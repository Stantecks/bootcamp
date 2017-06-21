import matplotlib.pyplot
import numpy
import seaborn as sns
sns.set(style='whitegrid')
%matplotlib inline

x = numpy.linspace(0, 2*numpy.pi, 200)
y = numpy.exp(numpy.sin(x))
matplotlib.pyplot.plot(x, y)
