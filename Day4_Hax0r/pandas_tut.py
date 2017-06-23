import pandas as pd

# Dictionary of top men's World Cup scorers and how many goals
wc_dict = {'Klose': 16,
           'Ronaldo': 15,
           'Müller': 14,
           'Fontaine': 13,
           'Pelé': 12,
           'Kocsis': 11,
           'Klinsmann': 11}

nation_dict = {'Klose': 'Germany',
               'Ronaldo': 'Brazil',
               'Müller': 'Germany',
               'Fontaine': 'France',
               'Pelé': 'Brazil',
               'Kocsis': 'Hungary',
               'Klinsmann': 'Germany'}

# Create a Series from the dictionary
s_goals = pd.Series(wc_dict)
s_nation = pd.Series(nation_dict)

# Take a look
s_goals
s_nation

# Combine into a DataFrame
df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})
