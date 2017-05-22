# importing libraries required
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
RANDOM_SEED = 2

# Loading the image and plotting it
y_img = mpimg.imread('mystery_number_scrambled.jpg')
imgplot = plt.imshow(y_img)

# Flattening the image into 1D array
y_img_flatten = y_img.flatten()

# Finding length of flattened image
n = len(y_img_flatten)
print "Length of flattened image: ", n

# Creating the suffled vector
random.seed(RANDOM_SEED)
vector = range(0, n)
random.shuffle(vector)

# Unscrambling the data
z_flat = -1*np.ones(n)
for index,originalIndex in enumerate(vector):
    z_flat[originalIndex] = y_img_flatten[index]

# Converting it back to 2D image and plotting the result
z_img = z_flat.reshape(480, -1)
imgplot = plt.imshow(z_img)
