# to install openCV : pip install opencv-python
# (Reading an image)------------->>>
# importing openCV library
import cv2

# reading the image
image = cv2.imread("openCV_basics/roadTraffic.jpg")

# saving the dimensions of the image in the h ,w variables
h, w = image.shape[:2]
print("height={}, width={}".format(h, w))

# Extracting the RGB value of pixel, Here we have chosen random value of an pixel by passing the 100, 100 for height and width
(G, B, R) = image[100, 100]
print("G={}, B={}, R={}".format(G, B, R))

# Extracting the region of interest (ROI)
# Slicing the pixels of the image
roi = image[100:400, 300:500]
# Creating the window to display the image
cv2.imshow("ROI", roi)
# The window will remain open until you press any key
cv2.waitKey(0)
a, b = roi.shape[:2]
print("height={}, width={}".format(a, b))

# Resize an image, resize() function takes two paremeters, the image and the dimensions
resize = cv2.resize(image, (100, 500))
cv2.imshow("resized Image", resize)
cv2.waitKey(0)