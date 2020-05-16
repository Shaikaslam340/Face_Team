import cv2
img=cv2.imread('alex.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('alex_copy.png',img)