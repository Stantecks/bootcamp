import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

bd_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
bd_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
bd_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
bd_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
bd_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

bd_1973['yearband'] = 1973
bd_1973 = bd_1973.rename(columns={'yearband' : 'year',
                                  'beak length' : 'beak length (mm)',
                                  'beak depth' : 'beak depth (mm)'
                                    })

bd_1975['year'] = 1975
bd_1975 = bd_1975.rename(columns={'Beak length, mm' : 'beak length (mm)',
                                  'Beak depth, mm' : 'beak depth (mm)'
                                    })


bd_1987['year'] = 1987
bd_1987 = bd_1987.rename(columns={'Beak length, mm' : 'beak length (mm)',
                                  'Beak depth, mm' : 'beak depth (mm)'
                                    })


bd_1991['year'] = 1991
bd_1991 = bd_1991.rename(columns={'blength' : 'beak length (mm)',
                                  'bdepth' : 'beak depth (mm)'
                                    })


bd_2012['year'] = 2012
bd_2012 = bd_2012.rename(columns={'blength' : 'beak length (mm)',
                                  'bdepth' : 'beak depth (mm)'
                                    })

bd_combined = pd.concat((bd_1973, bd_1975, bd_1987, bd_1991, bd_2012), ignore_index=True, axis=0)
