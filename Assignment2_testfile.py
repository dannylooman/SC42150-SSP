import matplotlib.pyplot as plt
import numpy as np

b1 = -1.996985042092529
b2 = 0.9989920170547919
b3 = 1.5795450691094583e-08

# initial conditions
N = 1000  # Number of Samples
x = np.zeros(N)
x[0] = 0
x[1] = 0
omega = np.random.randn(N)

for k in range(2, N):
    x[k] = b3 * omega[k] - b1 * x[k - 1] - b2 * x[k - 2]

k = np.arange(0, N, 1)
# plot the x
ax = plt.subplot()
ax.plot(k, x)
ax.set(xlabel='time steps N', ylabel='realization of x(n)',
       title='Simulation of dynamical model')
ax.grid()
plt.show()
