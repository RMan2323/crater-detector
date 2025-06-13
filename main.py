from ultralytics import YOLO

model = YOLO("runs/detect/train12/weights/best.pt")

results = model.train(epochs=5, pretrained=True, save_period=1)