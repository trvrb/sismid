#!/usr/bin/env python

import argparse

import os
import sys
import numpy as np
import scipy.spatial.distance
import sqlite3
import matplotlib.pyplot as plt
from pyembedding import *
import multiprocessing

def parse_variable_pairs(col_names, variable_pairs_str):
	var_pairs = list()
	if variable_pairs_str is None:
		for v1 in col_names:
			for v2 in col_names:
				var_pairs.append((v1, v2))
	else:
		pair_strs = [x.strip() for x in variable_pairs_str.split(',')]
		for pair_str in pair_strs:
			var_names = [x.strip() for x in pair_str.split(':')]
			if len(var_names) != 2:
				raise Exception('{0} does not specify two variables separated by :.'.format(pair_str))
			for var_name in var_names:
				if not var_name in col_names:
					raise Exception('{0} does match a column in the database.'.format(var_name))
			var_pairs.append(tuple(var_names))
	
	return var_pairs

def parse_col_names(col_names_str):
	return [x.strip() for x in col_names_str.split(',')]

def parse_library_sizes(Ls_str):
	if Ls_str is None:
		return None
	
	# Try min:max:by syntax
	pieces = Ls_str.split(':')
	if len(pieces) == 3:
		Lmin, Lmax, by = [int(x) for x in pieces]
		return range(Lmin, Lmax+1, by)
	
	# Try comma syntax
	return [int(x) for x in Ls_str.split(',')]

def init_db(db_filename):
	db = sqlite3.connect(db_filename)
	
	db.execute('CREATE TABLE args (position INTEGER, value TEXT)')
	for i, arg in enumerate(sys.argv):
		db.execute('INSERT INTO args VALUES (?,?)', [i, arg])
	
	db.execute('''
		CREATE TABLE results
		(cause TEXT, effect TEXT, L INTEGER, replicate_id INTEGER, corr REAL)
	''')
	db.commit()
	
	return db

def run_all(db, columns, var_pairs, E, tau, Ls, n_reps, n_cores):
	if n_cores > 1:
		pool = multiprocessing.Pool(n_cores)
	else:
		pool = None
	rng = random.SystemRandom()
	
	for cause_var, effect_var in var_pairs:
		cause_vec = columns[cause_var]
		effect_vec = columns[effect_var]
		run_pair(db, cause_var, cause_vec, effect_var, effect_vec, E, tau, Ls, n_reps, pool, rng)

def run_pair(db, cause_var, cause_vec, effect_var, effect_vec, E, tau, Ls, n_reps, pool, rng):
	library = make_embedding(effect_vec, E, tau)
	assert library.shape[1] == E
	predicted = cause_vec[(E-1)*tau:]
	assert predicted.shape[0] == library.shape[0]
	
	print('Analyzing {0}-causes-{1}'.format(cause_var, effect_var))
	
	def L_callback(L, corrs):
		if corrs:
			print('  ...done.')
			
			for rep_id, corr in enumerate(corrs):
				db.execute(
					'''INSERT INTO results VALUES (?,?,?,?,?)''',
					[cause_var, effect_var, L, rep_id, corr]
				)
			db.commit()
		else:
			print('  L = {0} running...'.format(L))
	
	results_list = ccm(
		library, predicted, library, predicted,
		Ls=Ls, n_neighbors=E+1, n_replicates=n_reps, replace=False, distances=None,
		L_callback=L_callback, pool=pool, rng=rng
	)
	
	db.commit()

if __name__ == '__main__':
	# Construct arguments
	parser = argparse.ArgumentParser(
		description='Run a convergent cross-mapping (CCM) analysis.',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
	parser.add_argument(
		'input_filename', metavar='<input-file>', type=str, help='Input filename (SQLite format).'
	)
	parser.add_argument(
		'input_table_name', metavar='<input-table-name>', type=str, help='Name of data table in input file.'
	)
	parser.add_argument(
		'output_filename', metavar='<output-file>', type=str,
		help='Output filename (SQLite format).'
	)
	parser.add_argument(
		'--variable-pairs', '-V', metavar='<cause>:<effect>,<cause>:<effect>...', type=str,
		help='Pairs of variables to test for causality; cause and effect are separated by a colon (:) and pairs are separated by a comma (,).' +
		'If omitted, all pairs of variables corresponding to loaded table columns will be tested.'
	)
	parser.add_argument(
		'--library-sizes', '-L', metavar='<start-L>:<end-L>:<skip>|<L1,L2,...>', type=str,
		help='Sizes of prediction libraries to test. ' + 
			'<start-L>:<end-L>:<skip> will use <start-L>, <start-L> + <skip>, ..., <end-L>. ' + 
			'<end-L> will be included if it is equal to <start-L> + <skip>*N for some N. ' + 
			'If omitted, only the minimum and maximum possible library sizes will be used.'
	)
	parser.add_argument(
		'--n-replicates', '-R', metavar='<n-reps>', type=int, default=100,
		help='Number of replicates to run for each library size.'
	)
	parser.add_argument(
		'--embedding-dimension', '-E', metavar='<E>', type=int, default=3,
		help='Embedding dimension used for prediction.'
	)
	parser.add_argument(
		'--tau', '-t', metavar='<tau>', type=int, default=1,
		help='Time lag used to reconstruct attractor.'
	)
	parser.add_argument(
		'--columns', '-C', metavar='<col1>,<col2>,...', type=str,
		help='Columns to load from the SQLite table.'
	)
	parser.add_argument(
		'--filter', '-f', metavar='<filter>', type=str,
		help='SQL filter to select rows (requires SQLite input data). E.g., "time >= 100.0" will use "WHERE time >= 100.0" when reading rows.'
	)
	parser.add_argument(
		'--overwrite-output', '-o', action='store_true',
		help='Overwrite output file if it already exists.'
	)
	parser.add_argument(
		'--n-cores', '-p', type=int, default=1,
		help='Number of cores to distribute analyses onto.'
	)
	args = parser.parse_args()
	
	# Check input & output files
	if args.input_filename == args.output_filename:
		parser.exit('Input filename and output filename cannot be the same.')
	if os.path.exists(args.output_filename):
		if args.overwrite_output:
			os.remove(args.output_filename)
		else:
			parser.error('Output filename {0} exists. Delete it or use --overwrite-output.'.format(args.output_filename))
	
	# Load input data
	try:
		with sqlite3.connect(args.input_filename) as db:
			col_names, columns = read_table(
				db, args.input_table_name, col_names=parse_col_names(args.columns), filter=args.filter
			)
	except Exception as e:
		parser.error(e)
	
	# Parse variable pairs
	try:
		var_pairs = parse_variable_pairs(col_names, args.variable_pairs)
	except Exception as e:
		parser.error(e)
	
	Ls = parse_library_sizes(args.library_sizes)
	
	db = init_db(args.output_filename)
	run_all(db, columns, var_pairs, args.embedding_dimension, args.tau, Ls, args.n_replicates, args.n_cores)
