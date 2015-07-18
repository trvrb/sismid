# Mechanistic, history-based, two-strain model with sinusoidal forcing
# Implemented with the Euler method
# Modified from
# http://homepages.warwick.ac.uk/~masfz/ModelingInfectiousDiseases/Chapter4/Program_4.1/index.html

import numpy as np


def run_two_strain(end_time, output_interval, step_size, params, ic):

    gamma = params[0]
    mu = params[1]
    alpha = params[2]
    a = params[3]
    omega = params[4]
    beta0 = params[5]
    epsilon = params[6]

    def step_diff_eqs(s, h, t):
        dxdt = np.zeros(8)

        # transmission rates
        forcing = 1 + epsilon*np.cos(omega*t)
        beta_0 = beta0[0]*forcing
        beta_1 = beta0[1]*forcing

        # forces of infection
        lambda1 = beta_0*(s[1]+a[0]*s[6])
        lambda2 = beta_1*(s[4]+a[1]*s[3])

        dxdt[0] = mu - s[0] * (lambda1 + lambda2) - mu * s[0]
        dxdt[1] = s[0]*lambda1 - gamma[0]*s[1] - mu * s[1]
        dxdt[2] = gamma[0]*s[1] - alpha[1]*s[2]*lambda2 - mu * s[2]
        dxdt[3] = alpha[1]*s[2]*lambda2 - gamma[1]*s[3] - mu * s[3]
        dxdt[4] = s[0] * lambda2 - gamma[1]*s[4] - mu * s[4]
        dxdt[5] = gamma[1]*s[4] - alpha[0]*s[5]*lambda1 - mu * s[5]
        dxdt[6] = alpha[0]*s[5]*lambda1 - gamma[0]*s[6] - mu * s[6]
        dxdt[7] = gamma[0] * s[6] + gamma[1]*s[3] - mu * s[7]
        return s + np.dot(dxdt, h)

    output = []
    state_vars = ic
    t = 0
    t_next_output = t + output_interval
    while t < t_next_output and t < end_time:
        state_vars = step_diff_eqs(state_vars, step_size, t)
        t += step_size
        if t >= t_next_output:
            output.append(state_vars)
            t_next_output += output_interval

    output = np.asarray(output)
    return output
