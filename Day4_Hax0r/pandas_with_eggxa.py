import pandas as pd

# Read in data files with pandas with no row headings.
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

# Change column headings
df_low.columns = ['low']
df_high.columns = ['high']

# Concatenate DataFrames
df = pd.concat((df_low, df_high), axis=1)

# Tidy data (the dropna drops the entire row.
# After melt we only have one entry in the row)

df = pd.melt(df, var_name='food density',
             value_name='cross-sectional area (sq micron)').dropna()

inds = (df['food density'] == 'high') & (df['cross-sectional area (sq micron)'] > 2000)

df.to_csv('xa_combined.csv', index=False)

df_reloaded = pd.read_csv('xa_combined.csv')
