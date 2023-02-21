import cv2
import numpy as np

# Load an image from a file
img = cv2.imread('solidWhiteRight.jpg')

# if to be resized, else comment
# set new width and height
new_width = 640
new_height = 480

# resize image
resized_img = cv2.resize(img, (new_width, new_height))

# Convert to grayscale
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 7)

# Apply threshold to create binary image
ret, thresh = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY)

# Display the image
cv2.imshow('Thresh', thresh)
    
# Define region of interest
# Define the region of interest (ROI) as a rectangular area
x, y, w, h = 80, 300, 490, 480
roi_mask = np.zeros_like(thresh)
cv2.rectangle(roi_mask, (x, y), (x+w, y+h), (255, 255, 255), -1)

# Apply the mask to the input image using bitwise_and function
masked_img = cv2.bitwise_and(thresh, roi_mask)

# Apply Canny edge detection
# Define thresholds for edge detection
low_threshold = 50
high_threshold = 150
    
edges = cv2.Canny(masked_img, low_threshold, high_threshold)

# Apply Hough line transform to the edge-detected image
rho = 1
threshold = 200
min_line_length = 1
max_line_gap = 120
#lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
lines = cv2.HoughLinesP(edges, rho, np.pi/180, threshold, np.array([]), min_line_length, max_line_gap)

# Draw the detected lines on the input image
if lines is not None:
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(resized_img, (x1, y1), (x2, y2), 255, 5)
    """ for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(resized_img, (x1, y1), (x2, y2), (0, 0, 255), 2) """

# Display the image
cv2.imshow('Hough', resized_img)

# Wait for a key press to close the window
cv2.waitKey(0)

# Release resources
cv2.destroyAllWindows()
