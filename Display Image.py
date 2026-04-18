import cv2
img = cv2.imread('your_image.jpg')
cv2.imshow('My Image Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()