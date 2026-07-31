import numpy as np

from nonlinear import derivatives
from integrator import rk4_step
from parameters import *

t = 0
dt = 0.01

state = np.array([theta1, theta2, omega1, omega2], dtype=float)

history = []

while t < 30:

    history.append(state.copy())

    state = rk4_step(derivatives, t, state, dt)

    t += dt
    

print(history[:5])

import visualization

visualization.show_animation(history)