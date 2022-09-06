from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm
x_axis = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y_axis = norm.pdf(x_axis, 0, 2)
pyplot.plot(x_axis, y_axis)
pyplot.show()