###################################################################																   #
# Basic plot for two-strain SIR model:
# Bifurcation diagram for one parameter
####################################################################

import sys
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.font_manager import FontProperties 
import matplotlib.pyplot as plt
from two_strain import *

# Run parameters
run_num = 1  # sys.argv[1]
end_time = 1000*365
output_interval = 365.0  # if not 365., need to adjust strobe interval
step_size = 1.0
sweep_par = "beta[0]"  # e.g., "beta[0]", "a[1]", "alpha[0]"
par_min = 1.0/7.0
par_max = 7.0/7.0
n_points = 40  # number of points in parameter range
n_strobes = 50  # number of years to sample

# Strain parameters, including initial conditions
beta = np.array([5, 5])/7.0
epsilon = 0.1
gamma = np.array([1, 1])/7.0
mu = 1/(10*365.0)
alpha = np.array([1., 1.])
a = np.array([1., 1.])
omega = 2*np.pi/365.
obs_sd = 0.01

NSS = 0.2
NIS = 1e-3
NRS = 0.02
NRI = 0.0
NSI = 1e-3
NSR = 0.02
NIR = 0.0

# Organize and run simulations
SI = np.array([NSS, NIS, NRS, NRI, NSI, NSR, NIR])
ic = np.array([NSS, NIS, NRS, NRI, NSI, NSR, NIR, 1-np.sum(SI)])
par_vals = np.linspace(par_min, par_max, n_points)
bif_vals = np.zeros((len(par_vals), n_strobes))
for i in range(len(par_vals)):
    print('Running value %d of %d' % (i+1,len(par_vals)))
    exec(sweep_par + " = par_vals[i]")
    params = np.array([gamma, mu, alpha, a, omega, beta, epsilon])
    output = run_two_strain(end_time, output_interval, step_size, params, ic)
    I = output[:, 1] + output[:, 6]  # NIS + NIR
    bif_vals[i, :] = I[-n_strobes:len(I)]

# Plot output
plt.plot(par_vals, bif_vals, '.k')
plt.xlabel(sweep_par)
plt.ylabel("NIS + NIR")
plt.xlim([par_min, par_max])
plt.show()
plt.savefig("bifurcation_" + sweep_par + ".png")
plt.close()
