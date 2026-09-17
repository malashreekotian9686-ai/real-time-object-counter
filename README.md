# Real-Time Object Counter

A real-time object detection and counting system developed using Python, YOLO, OpenCV, and Flask. The system detects objects from a live camera feed and displays their counts through a web-based interface.

## 📌 Project Overview

The **Real-Time Object Counter** is a computer vision application that detects and counts objects from a live webcam feed.

The system uses the **YOLO object detection model** to identify objects in real time. OpenCV is used for camera and video processing, while Flask provides a web-based interface for displaying the live detection results.

The application can detect multiple objects in a video stream and display their corresponding counts in real time.

## ✨ Features

- Real-time object detection
- Real-time object counting
- Webcam/video stream processing
- YOLO-based object detection
- OpenCV-based image and video processing
- Web-based interface using Flask
- Detection of multiple object types
- Live display of detected objects and their counts

## 🛠️ Technologies Used

- **Python** – Core programming language
- **YOLO** – Object detection model
- **OpenCV** – Image and video processing
- **NumPy** – Numerical and array operations
- **cvzone** – Computer vision utilities
- **Flask** – Web application framework
- **HTML** – Web interface structure
- **CSS** – Web interface styling

## 🔄 System Workflow

```text
Webcam / Video Input
        ↓
OpenCV Video Capture
        ↓
YOLO Object Detection
        ↓
Object Identification
        ↓
Object Counting
        ↓
Flask Web Application
        ↓
Real-Time Results
```

## 📸 Screenshots

Screenshots of the running application will be added here.

### Real-Time Object Detection

![Real-Time Object Detection](screenshots/object-detection.png)

### Object Counting

![Object Counting](screenshots/object-counting.png)

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/malashreekotian9686-ai/real-time-object-counter.git
```

### 2. Navigate to the Project Directory

```bash
cd real-time-object-counter
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```powershell
venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

After installing the required dependencies, run the Flask application:

```bash
python app.py
```

Then open a web browser and visit:

```text
http://127.0.0.1:5000
```

The application will display the live camera feed and detected object counts.

## 📁 Project Structure

```text
real-time-object-counter/
│
├── app.py
├── camera.py
├── object_counter.py
├── object_detection.py
├── object_type_counter.py
├── webcam_test.py
├── yolo_test.py
│
├── yolov8n.pt
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .gitignore
└── README.md
```

## 📂 Main Components

### `app.py`
Runs the Flask web application and handles the web interface.

### `camera.py`
Handles camera input and video frame processing.

### `object_detection.py`
Contains the object detection functionality using YOLO.

### `object_counter.py`
Handles object counting operations.

### `object_type_counter.py`
Counts detected objects according to their object types.

### `yolov8n.pt`
YOLO model weights used for object detection.

### `templates/index.html`
Contains the structure of the web interface.

### `static/style.css`
Contains the styling for the web interface.

## 🎯 Applications

The system can be adapted for:

- People counting
- Vehicle counting
- Traffic monitoring
- Retail monitoring
- Crowd monitoring
- Smart surveillance
- Industrial monitoring
- Computer vision applications

## 🚀 Future Enhancements

- Improved object tracking
- Support for multiple camera sources
- Object counting statistics
- Database integration for storing results
- Additional object detection classes
- Cloud deployment
- Improved real-time processing performance

## 👩‍💻 Author

**Malashree**

MCA Student | Aspiring Software Developer