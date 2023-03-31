import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Loading known faces
aditya_image = face_recognition.load_image_file("faces/aditya.jpg")
aditya_encoding = face_recognition.face_encodings(aditya_image)[0]

priyanka_image = face_recognition.load_image_file("faces/priyanka.jpg")
priyanka_encoding = face_recognition.face_encodings(priyanka_image)[0]

known_face_encodings = [aditya_encoding, priyanka_encoding]
known_face_names = ["Aditya", "Priyanka"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# csv writer
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognizing faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            top, right, bottom, left = location
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Adding text if the person is present
            if name in students:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (left, bottom + 25)
                fontScale = 1
                fontColor = (0, 255, 0)
                thickness = 2
                lineType = 2

                cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

                students.remove(name)
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture
video_capture.release()

# Wait for a small delay to allow the callback to finish
cv2.waitKey(500)

# Destroy all windows
cv2.destroyAllWindows()

# Close the csv file
f.close()
