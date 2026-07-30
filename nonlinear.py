"""
Nonlinear equations of motion for a planar double pendulum.

Derived using the Euler–Lagrange equations.
Integrated numerically using the fourth-order Runge–Kutta (RK4) method.
"""

import numpy as np
from parameters import *

def derivatives(t, state):
    theta1, theta2, omega1, omega2 = state

    dtheta1 = omega1
    dtheta2 = omega2

    domega1 = (
    -g * (2*m1 + m2) * np.sin(theta1)
    - m2 * g * np.sin(theta1 - 2*theta2)
    - 2 * np.sin(theta1 - theta2) * m2 * (
        omega2**2 * L2
        + omega1**2 * L1 * np.cos(theta1 - theta2)
        )
    ) / (
        L1 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    )

    domega2 = (
        2 * np.sin(theta1 - theta2) * (
            omega1**2 * L1 * (m1 + m2)
            + g * (m1 + m2) * np.cos(theta1)
            + omega2**2 * L2 * m2 * np.cos(theta1 - theta2)
        )
    ) / (
        L2 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    )

    return np.array([
        dtheta1,
        dtheta2,
        domega1,
        domega2
    ])