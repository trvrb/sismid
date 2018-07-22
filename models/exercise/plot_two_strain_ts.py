###################################################################																   #
# Basic plot for two-strain SIR model:
# Time series given some initial conditions
####################################################################

import sys
import csv
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.font_manager import FontProperties 
import matplotlib.pyplot as plt
from two_strain import *

# Run parameters
run_num = 1  # sys.argv[1]
end_time = 100*365
output_interval = 1.0
step_size = 0.1

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

# Organize and run simulation
params = np.array([gamma, mu, alpha, a, omega, beta, epsilon])
SI = np.array([NSS, NIS, NRS, NRI, NSI, NSR, NIR])
ic = np.array([NSS, NIS, NRS, NRI, NSI, NSR, NIR, 1-np.sum(SI)])
output = run_two_strain(end_time, output_interval, step_size, params, ic)

# Save output (NIS+NIR, NSI+NRI) to csv and plot
infecteds = np.asarray([output[:, 1] + output[:, 6], output[:, 3] + output[:, 4]])
times = np.arange(0,infecteds.shape[1])
infecteds_t = np.vstack((times, infecteds))
filename = 'infecteds_' + str(run_num) + '.csv'
with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['times', 'I1', 'I2'])
    writer.writerows(infecteds_t.T)

# Add observation error if present
if obs_sd > 0:
    errors = np.random.normal(1, obs_sd, infecteds.shape)
    infecteds_obs = infecteds*errors
    filename = 'infecteds_obs_' + str(run_num) + '.csv'
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['times', 'I1', 'I2'])
        writer.writerows(infecteds_t.T)

plt.subplot(3, 1, 1)
plt.plot(output[:, 0], 'b-', label=r'$N_{SS}$')
plt.plot(output[:, 2], 'g-', label=r'$N_{RS}$')
plt.plot(output[:, 5], 'r-', label=r'$N_{SR}$')
plt.plot(output[:, 7], 'c-', label=r'$N_{RR}$')
plt.xlabel('Time')
plt.ylabel('Uninfected')
plt.legend(loc=1, prop=FontProperties(size='smaller'))
plt.subplot(3, 1, 2)
plt.plot(output[:, 1], 'b-', label=r'$N_{IS}$')
plt.plot(output[:, 6], 'g-', label=r'$N_{IR}$')
plt.plot((output[:, 1]+a[0]*output[:, 6]), 'r-', label=r'$I_1$')
plt.xlabel('Time')
plt.ylabel('Infected 1')
plt.legend(loc=1, prop=FontProperties(size='smaller'))
plt.subplot(3, 1, 3)
plt.plot(output[:, 4], 'b-', label=r'$N_{SI}$')
plt.plot(output[:, 3], 'g-', label=r'$N_{RI}$')
plt.plot((output[:, 4]+a[1]*output[:, 3]), 'r-', label=r'$I_2$')
plt.xlabel('Time')
plt.ylabel('Infected 2')
plt.legend(loc=1, prop=FontProperties(size='smaller'))
plt.savefig("time_series_" + str(run_num) + ".png")
plt.show()
plt.close()
