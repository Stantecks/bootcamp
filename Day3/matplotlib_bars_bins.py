import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

# Reset bins, since xa_low has smaller values
bins = np.arange(1600, 2501, 50)


xa_low = np.loadtxt('data/xa_low_food.csv', comments ='#')
# Set up a figure with set of axes
fig, ax = plt.subplots(1, 1)

# Add axis labels
ax.set_xlabel('Cross-sectional area (µm$^2$)')
ax.set_ylabel('count');

# Generate the histogram for the low-density fed mother
_ = ax.hist(xa_low, bins=bins)

# Save the figure
fig.savefig('practice_histogram.pdf')

# Show the plot
plt.show()
