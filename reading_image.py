import cv2

# Load an image from a file
img = cv2.imread('lane_detection\solidWhiteRight.jpg')

# if to be resized, else comment
# set new width and height
new_width = 640
new_height = 480

# resize image
resized_img = cv2.resize(img, (new_width, new_height))

# Display the image
cv2.imshow('image', resized_img)

# Wait for a key press to close the window
cv2.waitKey(0)

# Release resources
cv2.destroyAllWindows()
