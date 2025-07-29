from ultralytics import YOLO
import cv2

model = YOLO("best_Model.pt")  
video_path = r"C:\Users\aswin\Desktop\YOLO\Aware_Dog\Test_Video\Real Aggressive Dog.mp4"
cap = cv2.VideoCapture(video_path)

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter("output_result.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

  
    results = model.predict(source=frame, imgsz=640, conf=0.25, device=0, verbose=False)

   
    annotated_frame = results[0].plot()

    
    out.write(annotated_frame)

    
    cv2.imshow("YOLOv11n Inference", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
