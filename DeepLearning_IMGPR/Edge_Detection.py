import cv2

img = cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//2.png", 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()