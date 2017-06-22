import numpy as np
# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns


def bohr_parameter(c, RK, Kda=0.017, Kdi=0.002, Kswitch=5.8):
    """Attempt to data collapse the fold-change induction"""
    first_term = -np.log(RK)
    top_term = (1 + (c / Kda))**2
    bot_term = (1 + (c / Kda))**2 + Kswitch * (1 + (c / Kdi))**2
    second_term = np.log(top_term / bot_term)
    bohr = first_term - second_term
    return bohr


def fold_change_bohr(bohr_parameter):
    """Calculates fold change in terms of the bohr parameter"""
    bot_term = 1 + np.exp(-bohr_parameter)
    inv_term = 1 / bot_term
    return inv_term


# Graph Settings
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Data Extraction
data_wt = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')
data_q18a = np.loadtxt('data/q18a_lac.csv', skiprows=3, delimiter=',')
data_q18m = np.loadtxt('data/q18m_lac.csv', skiprows=3, delimiter=',')

# Data slicing
wt_x = data_wt[:, 0]
q18a_x = data_q18a[:, 0]
q18m_x = data_q18m[:, 0]
wt_y = data_wt[:, 1]
q18a_y = data_q18a[:, 1]
q18m_y = data_q18m[:, 1]

# Generate theoretical points
theo_conc = np.logspace(-7, 1)
bohr_values = np.linspace(-6, 6, 200)
bohr_param = bohr_parameter(theo_conc, 16)

# Get bohr parameters
bohr_wt = bohr_parameter(wt_x, 141.5)
bohr_q18a = bohr_parameter(q18a_x, 16.56)
bohr_q18m = bohr_parameter(q18m_x, 1332)


fig, ax = plt.subplots(1, 1)

# fold change vs conc axis
# _ = ax.set_xlabel('IPTG (mM)')
# _ = ax.set_ylabel('fold change')
# _ = ax.set_xscale('log')

# fold change vs bohr axis
_ = ax.set_xlabel('Bohr Parameter')
_ = ax.set_ylabel('Fold Change')


# graphing in fold change in terms bohr_parameter
# _ = ax.plot(wt_x, wt_y, marker='.', linestyle='none')
# _ = ax.plot(q18m_x, q18m_y, marker='.', linestyle='none')
# _ = ax.plot(q18a_x, q18a_y, marker='.', linestyle='none')
# _ = ax.plot(theo_conc, fold_change_bohr(bohr_param), marker='.')

# graphing in fold change vs bohr_param
_ = ax.plot(bohr_values, fold_change_bohr(bohr_values), marker='.')
_ = ax.plot(bohr_wt, wt_y, marker='.', linestyle='none')
_ = ax.plot(bohr_q18a, q18a_y,
            marker='.', linestyle='none')
_ = ax.plot(bohr_q18m, q18m_y,
            marker='.', linestyle='none')

plt.show()
