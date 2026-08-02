import numpy as np

MAX_TRAIL = 1000 # in ticks
g = 9.81

m1 = 1.0
m2 = 1.0

L1 = 1.0
L2 = 1.0

# Update rule
t = 0
dt = 0.01
MAX_TIME = 30

# Initial Condition
theta1 = np.pi / 20
theta2 = np.pi

omega1 = 0.0
omega2 = 0.0
