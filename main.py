from ultralytics import YOLO

model = YOLO("runs/detect/train11/weights/best.pt")

results = model.train(epochs=2, pretrained=True, save_period=1)