import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    results = model(img)

    object_counts = {}

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])

            name = model.names[cls]

            if name in object_counts:
                object_counts[name] += 1
            else:
                object_counts[name] = 1

    annotated_frame = results[0].plot()

    y = 30

    for obj, count in object_counts.items():

        cv2.putText(
            annotated_frame,
            f"{obj}: {count}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        y += 30

    cv2.imshow("Object Type Counter", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()