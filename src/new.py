# Import library


import matplotlib.pyplot as plt
import matplotlib as mpl

COLOR = 'white'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR
# Define Data

x = [5, 6, 3.5, 9.3, 6.8, 9]
y = [2, 3, 6, 8, 15, 6.5]
  
# Plot Graph

plt.plot(x,y)
ax=plt.axes()

# Set color

ax.set_facecolor('pink')

# Display Graph

plt.show()