import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data) + 1 / len(data))
    return x, y


colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

data_hi = np.loadtxt('data/xa_high_food.csv', comments='#')
data_lo = np.loadtxt('data/xa_low_food.csv', comments='#')

fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('X')
_ = ax.set_ylabel('ECDF')
_ = ax.plot(*ecdf(data_hi), marker='.', linestyle='none')
_ = ax.plot(*ecdf(data_lo), marker='.', linestyle='none')


plt.show()
