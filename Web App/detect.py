from ultralytics import YOLO
import cv2
import os

model = YOLO('best.pt')

def run_detection(image_path, output_dir):
    results = model(image_path)
    result = results[0]

    img = cv2.imread(image_path)

    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, img)

    return output_path