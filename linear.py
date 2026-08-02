"""
Linear equations of motion for a planar double pendulum.

"""

import numpy as np
from parameters import *

def linear_derivatives(t, state):
    theta1, theta2, omega1, omega2 = state

    dtheta1 = omega1
    dtheta2 = omega2

    domega1 = (-g * ((m1 + m2) * theta1 - m2 * theta2)) / (m1 * L1)

    domega2 = (g * (m1 + m2) / (m1 * L2)) * (theta1 - theta2)

    return np.array([
        dtheta1,
        dtheta2,
        domega1,
        domega2
    ])