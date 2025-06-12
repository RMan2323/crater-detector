from ultralytics import YOLO

model = YOLO("runs/detect/train10/weights/best.pt")

results = model.train(epochs=5, pretrained=True, save_period=1)