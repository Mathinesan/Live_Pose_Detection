from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')##object detection


results = model(source= r"C:\Users\lenovo\Myenv\Pose.mp4" pose detection , show=True, conf=0.4, save=True)
