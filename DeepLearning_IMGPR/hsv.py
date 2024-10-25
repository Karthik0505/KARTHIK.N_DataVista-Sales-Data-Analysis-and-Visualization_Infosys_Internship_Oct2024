import cv2

img = cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//2.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()