from ultralytics import YOLO

model = YOLO("runs/detect/train17/weights/best.pt")

results = model.train(epochs=7, pretrained=True, save_period=1, half=True)