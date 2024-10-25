import cv2
import numpy as np

# Load the images
img1 = cv2.imread('C:/Users/GAGANKUMAR/OneDrive/Desktop/Infosys/Task3/img01.png')
img2 = cv2.imread('C:/Users/GAGANKUMAR/OneDrive/Desktop/Infosys/Task3/img02.png')

# Check if the images were loaded correctly
if img1 is None or img2 is None:
    print("Error: One or both images not found or cannot be opened.")
else:
    # Resize the images to 500x500
    img1 = cv2.resize(img1, (500, 500))
    img2 = cv2.resize(img2, (500, 500))

    # Concatenate images horizontally and vertically
    h_concat = np.hstack((img1, img2))
    v_concat = np.vstack((img1, img2))

    # Display the concatenated images
    cv2.imshow('Horizontal Concatenation', h_concat)
    cv2.imshow('Vertical Concatenation', v_concat)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
