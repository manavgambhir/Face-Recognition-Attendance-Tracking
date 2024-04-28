import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load known faces
manav_image = face_recognition.load_image_file("faces/manav.png")
manav_encoding = face_recognition.face_encodings(manav_image)[0]

babbar_image = face_recognition.load_image_file("faces/babbar.jpeg")
babbar_encoding = face_recognition.face_encodings(babbar_image)[0]

# xyz_image = face_recognition.load_image_file("faces/xyz.jpeg")
# xyz_encoding = face_recognition.face_encodings(xyz_image)[0]

known_face_encodings = [manav_encoding,babbar_encoding]
known_face_names = ["Manav","Babbar"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()           #_ is a random variable which tells if video capture successfully
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # Colour space conversion from BGR to RGB
    # OpenCv supports BGR but most other libraries use RGB

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame , face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)                 # Face encoding is mathematical representation of face
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            #Add the text if the person is present
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerofText = (10, 100)
                fontScale = 1.5
                fontColor = (255,0,0)
                thickness=3
                lineType=2
                cv2.putText(frame, name+" Present", bottomLeftCornerofText, font, fontScale, fontColor, thickness, lineType)

                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close the video capture and CSV file
video_capture.release()
cv2.destroyAllWindows()
f.close()

