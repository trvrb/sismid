############################################################
# Very simple fitting with Nelder-Mead
############################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from scipy.optimize import fmin, minimize
from two_strain import *

# Fitting parameters
# Parameter to fit is specified below
initial_guess = 0.8  # initial guess for optimization

# Fixed run parameters (for guesses and data)
output_interval = 1.0
end_time = 100*365.
step_size = 0.5

# Default parameters, including initial conditions
# (If importing data, consider whether you want the true values below.)
beta = np.array([5, 5]) / 7.0
epsilon = 0.01
gamma = np.array([1, 1]) / 7.0
mu = 1 / (10 * 365.0)
alpha = np.array([1., 1.])
a = np.array([1., 1.])
omega = 2 * np.pi / 365.

NSS = 0.1
NIS = 1e-3
NRS = 0.02
NRI = 0.0
NSI = 1e-3
NSR = 0.02
NIR = 0.0

I = np.array([NSS, NIS, NRS, NRI, NSI, NSR, NIR])
ic = np.array([NSS, NIS, NRS, NRI, NSI, NSR, NIR, 1 - np.sum(I)])

# Generate data...
parameters = np.array([gamma, mu, alpha, a, omega, beta, epsilon])
output = run_two_strain(end_time, output_interval, step_size, parameters, ic)
data = np.asarray([output[:, 1] + output[:, 6], output[:, 3] + output[:, 4]])

# ...OR load data from file, removing times column
# input_filename = 'infecteds_1.csv'  # (optional) file from which to import observations
# data = np.genfromtxt(input_filename, delimiter=',', skip_header=True)
# data = data[:, 1:]
# data = data.T


def error_function(guess_par):
    # beta = np.array([guess_par, 5/7.])  # sample input
    opt_pars = np.array([gamma, mu, alpha, a, omega, beta, guess_par])
    output = run_two_strain(end_time, output_interval, step_size, opt_pars, ic)
    guess = np.asarray([output[:, 1] + output[:, 6], output[:, 3] + output[:, 4]])
    error = np.linalg.norm(guess[1] - data[1]) ** 2
    return error

opt = minimize(error_function, (0.7, 0.9), method='Nelder-Mead')
print opt