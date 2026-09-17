import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    results = model(img)

    count = 0

    for r in results:
        count = len(r.boxes)

    annotated_frame = results[0].plot()

    cv2.putText(
        annotated_frame,
        f"Total Objects: {count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Object Counter", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()