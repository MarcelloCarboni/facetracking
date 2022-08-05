import cv2
import numpy as np
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)
# Value of the buffer from the center of the face 
buffer = 30

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

    biggest_face = (0,0,0,0)
    if (len(faces) > 1):
        # Find biggest rectangle
        face_areas = []
        for face in faces:
            face_areas.append(face[2]*face[3])
        print(max(face_areas), faces.index(max(face_areas)))
        biggest_face = face_areas.index(max(face_areas))
    elif (len(faces) == 1):
        biggest_face = faces[0]
    else:
        biggest_face = (0,0,0,0)


    line_w = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    line_h = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cv2.line(frame, (int(line_w/2), 0), (int(line_w/2), int(line_h)), (255, 0, 0), 2)

    if (max(biggest_face) != 0):
        # Draw a rectangle around the faces
        cv2.rectangle(frame, (biggest_face[0], biggest_face[1]), (biggest_face[0]+biggest_face[2], biggest_face[1]+biggest_face[3]), (0, 255, 0), 2)
        cv2.line(frame, (int((biggest_face[0] + (biggest_face[2]/2)) + buffer), 0), (int((biggest_face[0] + (biggest_face[2]/2)) + buffer), int(line_h)), (0, 0, 255), 2)
        cv2.line(frame, (int((biggest_face[0] + (biggest_face[2]/2)) - buffer), 0), (int((biggest_face[0] + (biggest_face[2]/2)) - buffer), int(line_h)), (0, 0, 255), 2)

        # Move camera
        if (int((biggest_face[0] + (biggest_face[2]/2)) - buffer) > int(line_w / 2)): # if left
            print('left')
        elif (int((biggest_face[0] + (biggest_face[2]/2)) + buffer) < int(line_w / 2)):
            print('right')

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()