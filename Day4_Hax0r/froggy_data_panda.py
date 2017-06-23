import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Slice out big forces
df_big_force = df.loc[df['impact force (mN)'] > 1000, :]

df.loc[df['ID'] == 'I', ['impact force (mN)', 'adhesive force (mN)']]

# Impact times with adhesive strength greater than 2000 Pa
df.loc[df['adhesive strength (Pa)'].apply(np.abs) > 2000, ['impact time (ms)']]

# Impact force and adhesive force


# group our data by individual frogs
grouped = df.groupby('ID')

# Find mean of the columns
""" this found the mean of all of the other columns when grouped by
    just the frog ID.  So each frog's averages were extracted
    some did not make sense """
df_mean = grouped.apply(np.mean)

# Extract just the frogs and their impact forces
imp_force_df = df.loc[:, ['ID', 'impact force (mN)']]

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('impact force (mN)')
ax.set_ylabel('adhesive force (mN)')
_ = ax.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.',
            linestyle='none')

plt.show()

# quick plot
# df.plot(x='total contact area (mm2)', y='adhesive force (mN)', kind='scatter');
