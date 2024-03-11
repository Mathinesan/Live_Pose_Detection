from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')##object detection

#To specify the source for the camera in YOLOv8, you can use "source = 0" for the laptop camera and "source = 1" for the webcam

results = model(source= 0, show=True, conf=0.4, save=True)
