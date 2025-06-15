from ultralytics import YOLO

model = YOLO("runs/detect/train15/weights/best.pt")

results = model.train(epochs=6, pretrained=True, save_period=1, half=True)