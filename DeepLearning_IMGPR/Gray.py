import cv2

img = cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//2.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()