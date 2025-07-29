from ultralytics import YOLO
import torch

if __name__ == '__main__':
    torch.multiprocessing.freeze_support()  # Needed on Windows

    # Load a pretrained YOLOv11n model
    model = YOLO("yolo11n.pt")

    # Train the model
    train_results = model.train(
        data="data.yaml",  # Path to dataset configuration file
        epochs=50,         # Number of training epochs
        imgsz=640,         # Image size for training
        device="0"         # GPU id (use 'cpu' if no GPU)
    )
