import cv2

img = cv2.imread(r"X:\opencv_files\Image")

cv2.putText(
    img,
    "X:\opencv_files\Image",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

cv2.imshow("X:\opencv_files\Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
