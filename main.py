from ultralytics import YOLO

model = YOLO("runs/detect/train18/weights/best.pt")

results = model.train(epochs=8, pretrained=True, save_period=1, half=True)