from ultralytics import YOLO

if __name__ == '__main__':
    # Load the YOLO model
    model = YOLO("yolo11n.pt")

    # Train the model
    train_results = model.train(
        data="data.yaml",  # Path to dataset YAML
        epochs=50,  # Number of training epochs
        imgsz=640,  # Training image size
        device=0  # Use GPU (0) or CPU (-1)
    )
