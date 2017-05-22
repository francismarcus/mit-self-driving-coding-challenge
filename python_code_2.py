from numpy import genfromtxt
from scipy.ndimage.interpolation import shift

# Extracting the coordinates.
my_data = genfromtxt('circle.csv', delimiter=',', skip_header =1)
x_vals = my_data[:,1]
y_vals = my_data[:,2]

# Plotting to make sure it's a circle
plt.plot(my_data[:,2], my_data[:,1], 'ro')
plt.show()

#Finding the second order gradient
d2x = np.gradient(np.gradient(x_vals))
d2y = np.gradient(np.gradient(y_vals))

# Findign location of max 2nd order gradient
print np.argmax(d2x)+1
print np.argmax(d2y)+1
