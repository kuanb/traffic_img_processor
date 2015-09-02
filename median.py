import cv2
import os

allPhotos = []

path = 'imgs/'
for fn in os.listdir(path):
    current = path + fn
    if os.path.isfile(current):
        img = cv2.imread(current)
        allPhotos.append(img)

# check that all images are the same size
if all(x.shape == allPhotos[0].shape for x in allPhotos):

for img in allPhotos:
    print img.shape

# img = cv2.imread('0.jpg')
#
# px = img[100,100]
# print px

# plt.imshow(img)
# plt.show()