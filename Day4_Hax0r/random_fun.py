import numpy as np
import scipy.stats
import bootcamp_utils
# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

mu = 10
sigma = 1
x_rnd = np.random.normal(mu, sigma, size=100000)


# Make ECDF
x, y = bootcamp_utils.ecdf(x_rnd)

# Plot it
fig, ax = plt.subplots(1, 1)

# _ = ax.plot(x[::1000], y[::1000], marker='.',
#             linestyle='none', color='dodgerblue')

_ = ax.hist(x, bins=100)

# Random choice DNA string
''.join(np.random.choice(list('AGTC'), size=70))

# Shuffle a deck of cards
np.random.permutation(np.arange(52))

# Given a million cells and a chance to pick up mutation being 1e-5
# how many mutations do I accumulate
np.random.binomial(1000000, 1e-5)

# Theoretical CDF
# _ = ax.plot([0, 1], [0, 1], color='tomato')

plt.show()
