import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Load in the data

data = np.loadtxt('data/retina_spikes.csv', skiprows=2,
                  delimiter=',')

# Slice out time and voltage
t = data[:, 0]
V = data[:, 1]

fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('t (ms)')
_ = ax.set_ylabel('V (mµV)')

_ = ax.plot(t, V)

plt.show()
