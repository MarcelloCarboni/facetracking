import cv2
import numpy as np
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)
# Value of the buffer from the center of the face 
buffer = 5

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    line_w = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    line_h = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.line(frame, (int(x+(w/2) - buffer), 0), (int(x+(w/2) - buffer), int(line_h)), (0, 0, 255), 4)
        cv2.line(frame, (int(x-(w/2) - buffer), 0), (int(x-(w/2) - buffer), int(line_h)), (0, 0, 255), 4)

    cv2.line(frame, (int(line_w/2), 0), (int(line_w/2), int(line_h)), (255, 0, 0), 4)

    # Move camera
    

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()