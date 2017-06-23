import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import bootcamp_utils as boot

bee_weight = pd.read_csv('data/bee_weight.csv', comment='#')
bee_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

ax = boot.ecdf_plot(bee_weight, 'Weight', hue='Treatment', formal=False)

plt.show()
