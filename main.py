import numpy as np

from nonlinear import nonlinear_derivatives
from linear import linear_derivatives
from integrator import rk4_step
from parameters import *

t = t
dt = dt

linear_state = np.array([theta1, theta2, omega1, omega2], dtype=float)
nonlinear_state = np.array([theta1, theta2, omega1, omega2], dtype=float)

linear_history = []
nonlinear_history = []

while t < MAX_TIME:

    linear_history.append(linear_state.copy())
    nonlinear_history.append(nonlinear_state.copy())

    linear_state = rk4_step(linear_derivatives, t, linear_state, dt)
    nonlinear_state = rk4_step(nonlinear_derivatives, t, nonlinear_state, dt)

    t += dt
    

# print(history1[:5])
# print(history2[:5])

import visualization

visualization.show_animation(linear_history, nonlinear_history)