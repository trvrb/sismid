#!/usr/bin/env python

import os
SCRIPT_DIR = os.path.dirname(__file__)
import sys
import json
import subprocess
import argparse
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
from collections import OrderedDict
import sqlite3
import csv
from matplotlib import rc, rcParams


def plot_run(
    output_filename,
    db
):
    vars = [row[0] for row in db.execute('SELECT DISTINCT cause FROM results')]
    var1 = vars[0]
    var2 = vars[1]

    Ls = [row[0] for row in db.execute('SELECT DISTINCT L FROM results')]
    L_index = dict([(L, i) for i, L in enumerate(Ls)])
    replicates = [row[0] for row in db.execute('SELECT DISTINCT replicate_id FROM results')]
    replicate_index = dict([(replicate, i) for i, replicate in enumerate(replicates)])
    mat = numpy.zeros((len(Ls), len(replicates)), dtype=float)
    for L in Ls:
        for replicate in replicates:
            mat[(L_index[L], replicate_index[replicate])] = db.execute('SELECT corr FROM results WHERE cause = ? AND effect = ? AND L = ? AND replicate_id = ?',(var1, var2, L, replicate)).next()[0]
    

    fig = pyplot.figure(figsize=[10,5])
    pyplot.subplot(1,2,1)
    for l in range(0, len(Ls)-1):
        L=Ls[l]
        pyplot.scatter(L*numpy.ones(len(replicates)), mat[l,:], alpha=0.5, edgecolors='none')
    pyplot.ylim((0,1))
    fig.gca().set_ylabel(r'Correlation, $\rho$')
    fig.gca().set_xlabel(r'Library length, $L$')
    fig.gca().set_title(str(var1) + ' causing ' + str(var2))


    tmp = var1
    var1 = var2
    var2 = tmp
    for L in Ls:
        for replicate in replicates:
            mat[(L_index[L], replicate_index[replicate])] = db.execute('SELECT corr FROM results WHERE cause = ? AND effect = ? AND L = ? AND replicate_id = ?',(var1, var2, L, replicate)).next()[0]

    pyplot.subplot(1,2,2)
    for l in range(0, len(Ls)-1):
        L=Ls[l]
        pyplot.scatter(L*numpy.ones(len(replicates)), mat[l,:], alpha=0.5, edgecolors='none')
    pyplot.ylim((0,1))
    fig.gca().set_ylabel(r'Correlation, $\rho$')
    fig.gca().set_xlabel(r'Library length, $L$')
    fig.gca().set_title(str(var1) + ' causing ' + str(var2))

    pyplot.savefig(output_filename)
    pyplot.close(fig)


    

if __name__ == '__main__':
    # Construct arguments
    parser = argparse.ArgumentParser(
        description='Scatter plot of rho values over L.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'input_filename', metavar='<input-filename>', type=str,
        help='If extension is .sqlite, assumed to be the output database from a sweep. If extension is .json, assumed to be parameters for a single run.'
    )
    parser.add_argument(
        'output_filename', metavar='<output-filename>', type=str,
        help='Output filename for plot.'
    )
    args = parser.parse_args()
    
    if args.input_filename.endswith('.sqlite'):
        db = sqlite3.connect(args.input_filename)
    else:
        sys.stderr.write('Input filename must end with .sqlite or .json.\n')
        sys.exit(1)
    
    plot_run(
        args.output_filename,
        db=db
    )
    
    if db is not None:
        db.close()
