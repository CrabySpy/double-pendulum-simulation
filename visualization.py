import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from parameters import L1, L2, MAX_TRAIL, dt


def polar_to_cartesian(theta1, theta2):
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    return x1, y1, x2, y2


def show_animation(linear_history, nonlinear_history):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    time_text = fig.text(
        0.5, 0.98,
        "",
        ha="center",
        va="top",
        fontsize=12
    )

    # Left subplot
    ax1.set_title("Linear Model")
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect("equal")

    rod1, = ax1.plot([], [], "o-", lw=2)
    mass1, = ax1.plot([], [], "o", markersize=10)
    trail11, = ax1.plot([], [], lw=0.5)
    trail12, = ax1.plot([], [], lw=1.5)

    # Right subplot
    ax2.set_title("Nonlinear Model")
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect("equal")

    rod2, = ax2.plot([], [], "o-", lw=2)
    mass2, = ax2.plot([], [], "o", markersize=10)
    trail21, = ax2.plot([], [], lw=0.5)
    trail22, = ax2.plot([], [], lw=1.5)

    # Trail history
    l_trail1_x, l_trail1_y = [], []
    l_trail2_x, l_trail2_y = [], []

    n_trail1_x, n_trail1_y = [], []
    n_trail2_x, n_trail2_y = [], []

    frames = min(len(linear_history), len(nonlinear_history))

    def animate(i):
        t = i * dt
        time_text.set_text(f"t = {t:.2f} s")

        if i == 0:
            l_trail1_x.clear()
            l_trail1_y.clear()
            l_trail2_x.clear()
            l_trail2_y.clear()

            n_trail1_x.clear()
            n_trail1_y.clear()
            n_trail2_x.clear()
            n_trail2_y.clear()

        # Linear
        theta1, theta2 = linear_history[i][:2]

        x1, y1, x2, y2 = polar_to_cartesian(theta1, theta2)

        rod1.set_data([0, x1, x2], [0, y1, y2])
        mass1.set_data([x1, x2], [y1, y2])

        l_trail1_x.append(x1)
        l_trail1_y.append(y1)
        l_trail2_x.append(x2)
        l_trail2_y.append(y2)

        if len(l_trail1_x) > MAX_TRAIL:
            l_trail1_x.pop(0)
            l_trail1_y.pop(0)
            l_trail2_x.pop(0)
            l_trail2_y.pop(0)

        trail11.set_data(l_trail1_x, l_trail1_y)
        trail12.set_data(l_trail2_x, l_trail2_y)

        # Nonlinear
        theta1, theta2 = nonlinear_history[i][:2]

        x1, y1, x2, y2 = polar_to_cartesian(theta1, theta2)

        rod2.set_data([0, x1, x2], [0, y1, y2])
        mass2.set_data([x1, x2], [y1, y2])

        n_trail1_x.append(x1)
        n_trail1_y.append(y1)
        n_trail2_x.append(x2)
        n_trail2_y.append(y2)

        if len(n_trail1_x) > MAX_TRAIL:
            n_trail1_x.pop(0)
            n_trail1_y.pop(0)
            n_trail2_x.pop(0)
            n_trail2_y.pop(0)

        trail21.set_data(n_trail1_x, n_trail1_y)
        trail22.set_data(n_trail2_x, n_trail2_y)

        return (
            rod1, mass1, trail11, trail12,
            rod2, mass2, trail21, trail22,
            time_text
        )

    ani = FuncAnimation(
        fig,
        animate,
        frames=frames,
        interval=10,
        blit=False
    )



    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()