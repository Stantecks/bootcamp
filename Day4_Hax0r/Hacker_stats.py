import numpy as np
# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


def bs_replicate(data, func=np.mean):
    """Compute a bootsrap replicate from data"""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)


def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw bootstrap replicates from 1d data"""
    return bs_reps = [bs_replicate(data, func=func)
                      for _ in range(size)]


bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')


# Generate lots of replicates
n_reps = 100000

# Elegant Oneliner for above.  Example of list comprehension
bs_reps = [bs_replicate(bd_2012, func=np.mean) for _ in range(n_reps)]

# Compute the percentiles with np.percentile

# Compute ECDFs for 1975 and 2012
x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)


# Plot the ECDFs
# fig, ax = plt.subplots(1, 1)
# ax.set_xlabel('beak depth (mm)')
# ax.set_ylabel('ECDF')
#
# _ = ax.plot(x_bs, y_bs, marker='.',
#             linestyle='none', label='Bootstrap Sample')
# _ = ax.plot(x_2012, y_2012, marker='.',
#             linestyle='none', label='2012')
#
# ax.legend(loc='lower right')

plt.show()
