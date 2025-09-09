# Face Recognition Attendance Tracking System
A Python-based application that leverages facial recognition technology to automate the process of marking attendance. The system detects faces in real-time via a webcam, identifies the individuals, and records their attendance in a CSV file with a timestamp.

## Features
- Real-Time Face Detection: Uses the webcam to detect and recognize multiple faces in the video feed simultaneously.

- Automated Attendance Logging: Automatically records the name and time of recognized individuals into a .csv file.

- Simple User Enrollment: Includes a script to easily add new individuals to the recognition database by capturing their photos.

- Efficient and Fast: Built with optimized libraries for quick face detection and matching.

## Technologies Used
- Python: The core programming language for the project.

- OpenCV (cv2): For real-time video capture and image processing.

- face_recognition: For state-of-the-art face encoding and recognition.

- NumPy: For efficient numerical operations on image arrays.

- CSV & Datetime: Standard Python libraries used for logging attendance with timestamps.

