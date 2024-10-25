import cv2

img = cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//2.png")
resized = cv2.resize(img, (200, 200))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()