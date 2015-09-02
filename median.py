import cv2
import os
import numpy
import math

allPhotos = []

path = 'imgs/'
for fn in os.listdir(path):
    current = path + fn
    if os.path.isfile(current):
        img = cv2.imread(current)
        allPhotos.append(img)

# check that all images are the same size
if all(x.shape == allPhotos[0].shape for x in allPhotos):
    col = range(allPhotos[0].shape[0]-1)
    row = range(allPhotos[0].shape[1]-1)
    for c in col:
        for r in row:
            eachImageVals = {"r": [], "b": [], "g":[]}
            for img in allPhotos:
                vals = img[c,r]
                eachImageVals["r"].append(vals[0])
                eachImageVals["b"].append(vals[1])
                eachImageVals["g"].append(vals[2])
            for v in eachImageVals:
                eachImageVals[v] = numpy.median(numpy.array(eachImageVals[v]))
                eachImageVals[v] = math.trunc(eachImageVals[v])
            allPhotos[0][c,r] = [eachImageVals["r"],eachImageVals["g"],eachImageVals["b"]]

print 'finished'

cv2.imshow('image', allPhotos[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

