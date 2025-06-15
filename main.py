from ultralytics import YOLO

model = YOLO("runs/detect/train16/weights/best.pt")

results = model.train(epochs=1, pretrained=True, save_period=1, half=True)