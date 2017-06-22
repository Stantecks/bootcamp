import numpy as np

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

data_wt = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')
data_q18a = np.loadtxt('data/q18a_lac.csv', skiprows=3, delimiter=',')
data_q18m = np.loadtxt('data/q18m_lac.csv', skiprows=3, delimiter=',')

wt_x = data_wt[:, 0]
q18a_x = data_q18a[:, 0]
q18m_x = data_q18m[:, 0]
wt_y = data_wt[:, 1]
q18a_y = data_q18a[:, 1]
q18m_y = data_q18m[:, 1]

fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('IPTG (mM)')
_ = ax.set_ylabel('fold change')
_ = ax.set_xscale('log')
_ = ax.plot(wt_x, wt_y, marker='.', linestyle='none')
_ = ax.plot(q18m_x, q18m_y, marker='.', linestyle='none')
_ = ax.plot(q18a_x, q18a_y, marker='.', linestyle='none')

plt.show()
