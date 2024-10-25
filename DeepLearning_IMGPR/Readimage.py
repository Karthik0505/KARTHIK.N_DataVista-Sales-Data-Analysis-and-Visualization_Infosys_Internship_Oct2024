import cv2

image=cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//2.png")
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image.shape)