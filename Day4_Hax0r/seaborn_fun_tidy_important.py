import numpy as np
import pandas as pd

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# # Extract just the frogs and their impact forces
# imp_force_df = df.loc[:, ['ID', 'impact force (mN)']]

# # Group them by the ID and apply the mean function from numpy
# grouped = imp_force_df.groupby('ID')
# df_mean = grouped.apply(np.mean)

ax = sns.swarmplot(data=df, x='ID', y='impact force (mN)', hue='date')
ax.set_ylabel('impact force (mN)')
ax.set_xlabel('')
# The object legend has underscore so legend_
ax.legend_.remove()

plt.show()
