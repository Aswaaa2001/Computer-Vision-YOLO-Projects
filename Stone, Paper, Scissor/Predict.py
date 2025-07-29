from ultralytics import YOLO
import cv2

# Load the trained YOLO v11 model
model = YOLO("Yolov11Best_model.pt")

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLO object detection on the frame
    results = model(frame)
    
    # Display the results
    for result in results:
        annotated_frame = result.plot()  # Get the frame with bounding boxes
        cv2.imshow("YOLOv11 Live Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
