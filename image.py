import cv2
# Read image
img = cv2.imread("X:\opencv_files\Image")
# Display image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
