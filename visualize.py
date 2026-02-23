import cv2

path = r"X:\opencv_files\Image"
img = cv2.imread(path)

cv2.imshow("Image Display", img)
cv2.waitKey(0)
cv2.destroyAllWindows()