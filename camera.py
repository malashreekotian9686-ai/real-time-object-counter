import cv2
from ultralytics import YOLO
from datetime import datetime
import os
import time

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

object_counts = {}

total_objects = 0
detection_running = True
screenshot_count = 0

latest_frame = None

def generate_frames():

    global object_counts
    global total_objects
    

    while True:

        success, frame = cap.read()

        if not success:
            break

        global latest_frame
        latest_frame = frame.copy()
        results = model(frame, imgsz=320)

        object_counts = {}

        for r in results:
            for box in r.boxes:

                cls = int(box.cls[0])
                name = model.names[cls]

                object_counts[name] = object_counts.get(name, 0) + 1

        total_objects = sum(object_counts.values())

        frame = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', frame)

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               frame + b'\r\n')

def save_screenshot():

    global latest_frame
    global screenshot_count

    print("Capture button clicked")

    if latest_frame is not None:

        print("Frame available")

        if not os.path.exists("captures"):
            os.makedirs("captures")

        filename = datetime.now().strftime(
            "captures/capture_%Y%m%d_%H%M%S.jpg"
        )

        cv2.imwrite(filename, latest_frame)

        screenshot_count += 1

        print("Saved:", filename)
        print("Screenshot count:", screenshot_count)

        return True

    print("latest_frame is None")
    return False