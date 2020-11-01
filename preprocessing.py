from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                help="path to input image")
ap.add_argument("-east", "--east", type=str,
                help="path to input EAST text detector")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
                help="minimum probability required to inspect a region")
ap.add_argument("-w", "--width", type=int, default=320,
                help="resized image width (should be multiple of 32)")
ap.add_argument("-e", "--height", type=int, default=320,
                help="resized image height (should be multiple of 32)")
args = vars(ap.parse_args())

kernel = np.ones((3,3), np.uint8) 

# load the input image and grab the image dimensions
img = cv2.imread(args["image"])

#img = cv2.medianBlur(img,1)

#img = cv2.GaussianBlur(img,(1,1),cv2.BORDER_DEFAULT)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur = cv2.blur(gray)


image = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)
image = cv2.resize(image, (960, 800))

blur = cv2.blur(gray,(1,1))
cv2.imshow("img",image)

cv2.waitKey(0)
cv2.imwrite("new.jpg", image) 


"""
image = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)

image = cv2.resize(image, (960, 800))

#image = cv2.dilate(image,kernel,iterations = 1)

#image = cv2.resize(dilation, (960, 800))

#image = cv2.resize(image, (960, 800))

cv2.imwrite("new.jpg", image) 

cv2.imshow("img",image)

cv2.waitKey(0)

"""