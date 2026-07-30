def rk4_step(f, t, y, dt):
    k1 = f(t,y)
    k2 = f(t + dt/2, y + dt*k1/2)
    k3 = f(t + dt/2, y + dt*k2/2)
    k4 = f(t + dt, y + dt*k3)

    return y + dt*(k1 + 2*k2 + 2*k3 + k4)/6
