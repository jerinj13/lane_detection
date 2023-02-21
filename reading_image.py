import cv2

# Load an image from a file
img = cv2.imread('path_of_image_file')

# Display the image
cv2.imshow('image', img)

# Wait for a key press to close the window
cv2.waitKey(1)

# Release resources
cv2.destroyAllWindows()
