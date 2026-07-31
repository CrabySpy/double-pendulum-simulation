import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from parameters import L1, L2, MAX_TRAIL


def polar_to_cartesian(theta1, theta2):
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    return x1, y1, x2, y2


def show_animation(history):

    fig, ax = plt.subplots()

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)

    ax.set_aspect("equal")


    rod, = ax.plot([], [], "o-", lw=2)

    mass, = ax.plot([], [], "o", markersize=10)

    trail1, = ax.plot([], [], lw=0.5)
    trail2, = ax.plot([], [], lw=1.5)

    trail1_x = []
    trail1_y = []

    trail2_x = []
    trail2_y = []

    def animate(i):
        if i == 0:
            trail1_x.clear()
            trail1_y.clear()
            trail2_x.clear()
            trail2_y.clear()

        theta1 = history[i][0]
        theta2 = history[i][1]

        x1, y1, x2, y2 = polar_to_cartesian(theta1, theta2)

        rod.set_data(
            [0, x1, x2],
            [0, y1, y2]
        )

        mass.set_data(
            [x1, x2],
            [y1, y2]
        )

        trail1_x.append(x1)
        trail1_y.append(y1)
        trail2_x.append(x2)
        trail2_y.append(y2)
        if len(trail1_x) > MAX_TRAIL:
            trail1_x.pop(0)
            trail1_y.pop(0)
            trail2_x.pop(0)
            trail2_y.pop(0)

        trail1.set_data(trail1_x, trail1_y)
        trail2.set_data(trail2_x, trail2_y)

        return rod, mass, trail1, trail2


    ani = FuncAnimation(
        fig,
        animate,
        frames=len(history),
        interval=10,
        blit=True
    )

    plt.show()