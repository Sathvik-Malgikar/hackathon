import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow
from collections import Counter
from sklearn.cluster import KMeans


image=cv2.imread("mspaint.jpg")
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
type(image)
image.shape

# plt.imshow(gray,cmap='gray')
# plt.show()

resized=cv2.resize(image, (200,500))
plt.imshow(resized)
plt.show()