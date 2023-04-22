import cv2
import numpy as np

'''We use the filter2D function that takes 3 arguments:
source: source image, ddepth: indicates the depth of resulting image
and kernel, which we apply to the image'''
 
#Read image
image = cv2.imread('test.jpg')

#Define kernel
kernel1 = np.array([[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]])

#Define arguments for filter2D()
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()
