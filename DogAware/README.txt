
KV_PYNR - v3 2025-07-27 2:02am
==============================

# 🐶 AwareDog: Street Dog Aggression Detection using YOLOv11

A computer vision project to detect **aggressive behavior in street dogs** using **YOLOv11**, intended for real-time use on edge devices (e.g., Raspberry Pi). The model is trained for **accuracy on GPU** using `yolov11m.pt` and optimized for deployment.

---

## 📁 Project Structure

AwareDog/
├── train/ # Training images and labels
├── valid/ # Validation images and labels
├── test/ # Test images and labels
├── data.yaml # Dataset config
├── yolov11m.pt # Pretrained YOLOv11m model
├── Train_Case1.py # YOLO training script
├── README.md # Project documentation (this file)


---

## ⚙️ Environment Setup

1. **Clone your project** or navigate to your project directory.
2. **Create a virtual environment** (optional but recommended):

```
python -m venv yolov11env
source yolov11env/bin/activate  # On Windows: yolov11env\Scripts\activate
Install required packages:


pip install ultralytics opencv-python roboflow
If you're using GPU with CUDA 11.8:


pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
🧠 Dataset Overview
Source: Roboflow

Roboflow project: ac_dogs_aggression_detection_ac2001-ns3ah

Dataset license: CC BY 4.0

Dataset Link

🔍 data.yaml
yaml
Copy
Edit
train: ./train
val: ./valid
test: ./test

nc: 2
names: ['normal_dog', 'aggressive_dog']
🏋️‍♂️ Model Training (YOLOv11m)
Script: Train_Case1.py


from ultralytics import YOLO

# Load a base model
model = YOLO("yolov11m.pt")

# Train on the dataset
model.train(
    data="data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device=0  # GPU: 0 | CPU: 'cpu'
)

# Validate the model
model.val()
Run the script with:


python Train_Case1.py
📈 Training Output
After training completes, YOLO stores the results in:


runs/detect/train/
├── weights/
│   ├── best.pt
│   └── last.pt
├── results.png
├── confusion_matrix.png
🧪 Model Testing
To test or visualize prediction:

///////////////////////////////////////////////////////////

from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
model.predict(source="test", save=True, show=True)
📤 Export the Trained Model
For deployment or inference on edge devices:


model.export(format="onnx")     # Export to ONNX
model.export(format="tflite")   # TensorFlow Lite
🚀 Edge Deployment (Future)
For real-time use, deploy on:

Raspberry Pi with Coral TPU

Jetson Nano

ESP32-CAM (image streaming only)

Trigger actions when aggressive_dog is detected:

Turn on buzzer/siren

Send alerts (WhatsApp/Telegram)

Flash LED or record footage

📊 Sample Outputs
Filename	Detection Result
frame_001.jpg	Detected: normal_dog
frame_023.jpg	Detected: aggressive_dog

🔍 YOLOv11 Model Comparison
Model	Speed 🏃	Accuracy 🎯	Best Use Case
yolov11n	🚀 Fast	Moderate	Real-time on Pi/Jetson
yolov11m	⚖️ Balanced	High	GPU Training/Moderate Edge
yolov11l	🐢 Slow	Very High	Cloud inference

➡ Use yolov11m for training (better accuracy), then convert to yolov11n or quantized format for edge deployment.

👤 Author
Aswin Chandran
Robotics Software Engineer
 Nileshwar, Kasaragod, Kerala
📧 aswinchandran2001ac@gmail.com

📄 License
This project is licensed under the MIT License.
You are free to use, distribute, and modify with attribution.

🙏 Acknowledgments
Ultralytics YOLO

Roboflow for dataset management

OpenCV for image processing



---








