from ultralytics import YOLO

model = YOLO("vnop.pt")

model.predict(source="no1 test.jpg" , show= True, save= True)