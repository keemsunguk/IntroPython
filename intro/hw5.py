import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as mp
from PIL import Image

img2 = Image.open('/Users/keemsunguk/projects/intro/data/stbug.png')
imgplot = plt.imshow(img2)

img = mpimg.imread('/Users/keemsunguk/projects/intro/data/stbug.png')
img.shape
img1 = img[:,:,1]
img1plot = plt.imshow(img1, cmap='hot')

img2plot = plt.imshow(img1, cmap='Accent')

img3plot = plt.imshow(img1, cmap='viridis')

img3 = img2.resize( (700, 700), Image.BICUBIC)
img3.show()
img3.save('/Users/keemsunguk/projects/intro/data/hw4-1.png')

