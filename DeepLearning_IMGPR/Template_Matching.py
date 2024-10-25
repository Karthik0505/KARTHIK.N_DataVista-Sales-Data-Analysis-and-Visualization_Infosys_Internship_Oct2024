import cv2

img = cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//2.png",0)
template = cv2.imread("C://Users//KARTHIK//OneDrive//Desktop//INFOSYS//22.png", 0)
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()