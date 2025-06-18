from ultralytics import YOLO
import cv2
import os

model = YOLO('best.pt')

def run_detection(image_path, output_dir):
    results = model(image_path, conf=0.23)
    result = results[0]

    img = cv2.imread(image_path)
    crater_data = []

    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        crater_data.append((x1, y1, x2, y2))
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_image_path = os.path.join(output_dir, base_name + '_output.jpg')
    metadata_path = os.path.join(output_dir, base_name + '_craters.txt')

    cv2.imwrite(output_image_path, img)

    with open(metadata_path, 'w') as f:
        for x1, y1, x2, y2 in crater_data:
            f.write(f'{x1},{y1},{x2},{y2}\n')

    return output_image_path, metadata_path
