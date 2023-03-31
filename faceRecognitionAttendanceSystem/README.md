# Face Recognition Attendance System
This Python script uses the face_recognition library to recognize faces from a live video feed, and keeps track of the attendance of recognized faces in a CSV file. The script uses Haar Cascades to detect faces and face_recognition library to recognize and encode faces.

## Requirements
Python 3.x

OpenCV

face_recognition library

## Usage

1. Clone the repository: 
```
git clone https://github.com/aditya9-2/faceRecognitionAttendanceSystem

```

2. Install required libraries:
```
 pip install opencv-python 
 ```
 and
 ```
  pip install face-recognition
  ```

* Remember You have Virtual Studio Installer

* Go to:
```
https://visualstudio.microsoft.com/downloads/?q=build+tools

```


3. Place the images of faces to be recognized in the faces/ directory with a name in the format <name>.jpg (Whatever format you want to use)


4. Run the script: 
```
python faceRecognitionAttendanceSystem.py
```
5. The script will open a live video feed and recognize faces. The script will output the names of recognized faces on the video feed and save the names of recognized people and the current time in a CSV file.


## Configurable Parameters

* video_capture - The video capture device to use. Default is 0.
* known_face_encodings - The list of face encodings of known faces. Add your own face encodings here.
* known_face_names - The list of names of known faces. Add your own names here.
* students - The list of expected students. Add your own student names here.
* current_date - The current date in the format YYYY-MM-DD. Change the format as required.
* f - The file to write the attendance data to. Change the filename as required.


## Output
* The script will output the names of recognized faces on the video feed.
* The script will save the names of recognized people and the current time in a CSV file with the name as the current date in the format YYYY-MM-DD.csv.


## References
* [OpenCV](https://opencv.org)

* [face_recognition library](https://github.com/ageitgey/face_recognition)