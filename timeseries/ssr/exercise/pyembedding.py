#!/usr/bin/env python

import os
import sys
import random
import numpy as np
import scipy.spatial.distance
import csv
import sqlite3
import multiprocessing
import ctypes

def make_shared_array(A):
	shared_array_base = multiprocessing.Array(ctypes.c_double, A.size)
	shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
	shared_array = shared_array.reshape(A.shape)
	shared_array[:] = A
	
	return shared_array

def read_table(db, table_name, col_names=None, filter=None):
	rows = list()
	query = 'SELECT '
	if col_names:
		query += ','.join(col_names)
	else:
		query += '*'
	query += ' FROM {0}'.format(table_name)
	if filter:
		query += ' WHERE {0}'.format(filter)
	
	columns = dict()
	c = db.execute(query)
	if col_names is None:
		col_names = [x[0] for x in c.description]
	for col_name in col_names:
		columns[col_name] = list()
	for row in c:
		for i, col_name in enumerate(col_names):
			columns[col_name].append(float(row[i]))
	
	return (col_names, dict([
		(col_name, np.array(columns[col_name]))
		for col_name in col_names
	]))

def make_embedding(x, E, tau=1, verify_all=False):
	"""Create a matrix of lagged vectors of size E from vector x.
	
	The lagged vectors of length E form the rows of the matrix.
	
	>>> x = np.array([3.0, 1.7, 4.3, 5.4, 8.8, 9.6])
	>>> X = make_embedding(x, 3, verify_all=True)
	>>> X.shape == (4,3)
	True
	>>> np.sum(X[0,:] == [3.0, 1.7, 4.3])
	3
	>>> np.sum(X[1,:] == [1.7, 4.3, 5.4])
	3
	>>> np.sum(X[2,:] == [4.3, 5.4, 8.8])
	3
	>>> np.sum(X[3,:] == [5.4, 8.8, 9.6])
	3
	>>> X2 = make_embedding(x, 3, tau=2, verify_all=True)
	>>> X2.shape[0]
	2
	>>> X2.shape[1]
	3
	>>> np.sum(X2[0,:] == [3.0, 4.3, 8.8])
	3
	>>> np.sum(X2[1,:] == [1.7, 5.4, 9.6])
	3
	"""
	# Preconditions
	assert E > 0
	assert len(x.shape) == 1
	N = x.shape[0]
	vec_span = tau * (E - 1) + 1
	assert N >= vec_span
	
	vec_count = N - tau * (E - 1)
	X = np.zeros((vec_count, E))
	for i in range(E):
		start = tau * i
		X[:,i] = x[start:(start + vec_count)]
	
	# Postcondition: boundary checks
	assert np.sum(X[0,:] == x[0:tau*E:tau]) == E
	if verify_all:
		for i in range(vec_count):
			assert np.sum(X[i,:] == x[i:i + tau*E:tau]) == E
 	assert np.sum(X[-1,:] == x[-(1 + tau*(E-1))::tau]) == E
	
	return X

# def ccm(X_train, y_train, X_test, y_test, Ls, n_neighbors=None, n_replicates=100, replace=False, distances=None):
# 	if distances is None:
# 		distances = compute_distances(X_train, X_test)
# 	
# 	for L in Ls:
# 		print('L={0}'.format(L))
# 		for rep in range(n_replicates):
# 			print('rep={0}'.format(rep))
# 			indexes = np.random.choice(X_train.shape[0], size=L, replace=replace)
# 			y_pred = simplex_predict(
# 				X_train[indexes,:], y_train[indexes],
# 				x_test, y_test,
# 				n_neighbors=n_neighbors,
# 				distances=distances[indexes,:]
# 			)
# 			print np.corrcoef(y_test, y_pred)[0,1]

def compute_distances(A, B):
	distances = scipy.spatial.distance.cdist(A, B)
	distances[distances == 0.0] = np.inf
	return distances

def simplex_predict(X_train, Y_train, X_test, Y_test, n_neighbors=None, distances=None):
	assert X_train.shape[0] == Y_train.shape[0]
	assert X_test.shape[0] == Y_test.shape[0]
	
	assert X_train.shape[1:] == X_test.shape[1:]
	assert Y_train.shape[1:] == Y_test.shape[1:]
	
	d = X_train.shape[1]
	if n_neighbors is None:
		n_neighbors = d + 1
	assert n_neighbors >= d + 1
	
	# if test and training sets overlap, we need to be able to remove a test vector
	# if it shows up in nearest neighbors
	assert X_train.shape[0] > n_neighbors
	
	if distances is None:
		distances = compute_distances(X_train, X_test)
	assert distances.shape[0] == X_train.shape[0]
	assert distances.shape[1] == X_test.shape[0]
	
	# print n_neighbors
	
	Y_pred = np.zeros(Y_test.shape)
	for i in range(Y_test.shape[0]):
		neighbor_ind = np.argpartition(distances[:,i], range(n_neighbors))[:n_neighbors]
		neighbor_dist = distances[neighbor_ind,i]
		
		assert neighbor_dist[0] != 0.0
		assert not np.isnan(neighbor_dist[0])
		
		if np.isinf(neighbor_dist[0]):
			weights = np.ones(n_neighbors, dtype=float) / float(n_neighbors)
		else:
			weights = np.exp(-neighbor_dist / neighbor_dist[0])
			weights = weights / np.sum(weights)
# 		print weights
# 		print Y_train[neighbor_ind]
		Y_pred[i] = np.dot(weights, Y_train[neighbor_ind])
# 		print y_pred[i]
# 		sys.exit(1)
		
		#print neighbor_indices
		#for j in range(1, n_neighbors):
		#	assert distances[neighbor_indices[j],i] >= distances[neighbor_indices[j-1],i]
	
	return Y_pred

def ccm(X_train, y_train, X_test, y_test,
	Ls=None, n_neighbors=None, n_replicates=100, replace=False, distances=None,
	L_callback=None, rep_callback=None, pool=None, rng=None
):
	if rng is None:
		rng = random.SystemRandom()
	
	if Ls is None:
		if n_neighbors is None:
			Ls = [X_train.shape[1] + 2, X_train.shape[0]]
		else:
			Ls = [n_neighbors + 1, X_train.shape[0]]
	
	if distances is None:
		distances = compute_distances(X_train, X_test)
	
	if pool:
		X_train = make_shared_array(X_train)
		y_train = make_shared_array(y_train)
		X_test = make_shared_array(X_test)
		y_test = make_shared_array(y_test)
		distances = make_shared_array(distances)
	
	results_list = list()
	for index_L, L in enumerate(Ls):
		if L_callback:
			L_callback(L, None)
		
		n_reps_L = 1 if (X_train.shape[0] == L and not replace) else n_replicates
		
		arg_list = list()
		for rep_id in xrange(n_replicates):
			seed = rng.randint(1, 2**32 - 1)
			arg_list.append((
				X_train, y_train, X_test, y_test, L, n_neighbors, replace, distances, rep_id, seed,
				None if pool else rep_callback
			))
		
		if pool:
			corrs = pool.map(ccm_single_mappable, arg_list)
		else:
			corrs = map(ccm_single_mappable, arg_list)
		
		if L_callback:
			L_callback(L, corrs)
		
		results_list.append([L, corrs])
	return results_list

def ccm_single_mappable(arg):
	return ccm_single(*arg)

def ccm_single(X_train, y_train, X_test, y_test, L, n_neighbors, replace, distances, rep_id, seed, rep_callback):
	rng = np.random.RandomState(seed)
	indexes = rng.choice(X_train.shape[0], size=L, replace=replace)
	X_train_rep = X_train[indexes,:]
	y_train_rep = y_train[indexes]
	y_pred = simplex_predict(
		X_train_rep, y_train_rep,
		X_test, y_test,
		n_neighbors=n_neighbors,
		distances=distances[indexes,:]
	)
	corr = np.corrcoef(y_test, y_pred)[0,1]
	if np.isnan(corr):
		corr = 1.0
	
	if rep_callback:
		rep_callback(L, corr, indexes, X_train_rep, y_train_rep, y_pred)
	
	return corr

if __name__ == '__main__':
	os.chdir(os.path.dirname(__file__))
	
	import doctest
	doctest.testmod(verbose=True)
