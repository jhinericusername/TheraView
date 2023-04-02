<<<<<<< HEAD
import cv2

# read the video file
cap = cv2.VideoCapture('jj.mp4')

# initialize an empty list to store frames
frames = []

# loop through all the frames in the video
while (cap.isOpened()):
    # read a frame from the video
    ret, frame = cap.read()
    # if the frame is read correctly
    if ret == True:
        # append the frame to the list of frames
        frames.append(frame)
    else:
        break

# release the video capture object
cap.release()

# print the number of frames extracted
print('Extracted', len(frames), 'frames from the video')

# display the first frame as an example
cv2.imshow('First Frame', frames[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
=======
import cv2

# read the video file
cap = cv2.VideoCapture('jj.mp4')

# initialize an empty list to store frames
frames = []

# loop through all the frames in the video
while (cap.isOpened()):
    # read a frame from the video
    ret, frame = cap.read()
    # if the frame is read correctly
    if ret == True:
        # append the frame to the list of frames
        frames.append(frame)
    else:
        break

# release the video capture object
cap.release()

# print the number of frames extracted
print('Extracted', len(frames), 'frames from the video')

# display the first frame as an example
cv2.imshow('First Frame', frames[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> bf3604ec78f035b027b5e839b5305601cdded50f
