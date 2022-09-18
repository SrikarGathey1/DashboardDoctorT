from PIL import Image
import matplotlib.pyplot as plt
import numpy

time = numpy.arange(0, 10, 0.001)
amplitude = numpy.sin(time)


# plt.plot(time, amplitude)

plt.xlabel('Time')
plt.ylabel('Flow')
plt.title('Breath Analysis')
plt.legend(['Flow'])
plt.grid("x") 



# save the figure
plt.savefig('plot1.png', dpi=300, bbox_inches='tight')

basewidth = 400
img = Image.open('plot1.png')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
img.save('resized_plot1.png')