import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('D:\Github\lane_detection\solidWhiteRight.mp4')

# check if the video was successfully opened
if not cap.isOpened():
    print("Error opening video file")

# loop through the frames of the video
while cap.isOpened():
    # read the next frame
    ret, frame = cap.read()

    # check if there was an error reading the frame
    if not ret:
        break

    # display the frame
    cv2.imshow('Video', frame)

    # wait for a key event to exit
    if cv2.waitKey(1) == ord('q'):
        break

# release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()
