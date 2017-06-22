import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Specify constants parameter
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8

# Specify my little time step
delta_t = 0.01

# Make an array of time points, evenly spaced up to 60
t = np.arange(0, 60, delta_t)

# Make array to store number of rabbits and foxicies
r = np.empty_like(t)
f = np.empty_like(t)

# Set the initial number of rabbits and fox
r[0] = 10
f[0] = 1

# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * (alpha * r[i-1] - beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('time')
ax.set_ylabel('population')
_ = ax.plot(t, r, label='rabbits')
_ = ax.plot(t, f, label='foxices')
_ = ax.legend()

plt.show()
