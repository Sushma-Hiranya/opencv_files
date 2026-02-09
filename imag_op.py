import cv2

img = cv2.imread("X:\opencv_files\Image")

# Safety check
if img is None:
    print("Image not found")
    exit()

# Image properties
height, width, channels = img.shape
size = img.size
datatype = img.dtype

print("Width :", width)
print("Height :", height)
print("Channels :", channels)
print("Image Size :", size)
print("Data Type :", datatype)
