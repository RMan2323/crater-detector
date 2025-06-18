# crater-detector using YOLOv8n
Requires the ultralytics package

## Using the Model
See the YOLO documentation [here](https://docs.ultralytics.com/modes/predict/).

## Using the Web App
This web application allows you to detect lunar craters using a trained YOLOv8 model. It supports both image uploads and live detection through a webcam.

Requirements:
* Python 3.7 or higher
* Pip (Python package manager)

To set up for the first time:

1. Go to the "Web App" directory
2. Open the Terminal or CLI
3. Run the command "pip install -r requirements.txt"

To run the app:
1. Go to the "Web App" directory
2. Open the Terminal or CLI
3. Run the command "python3 app.py"
4. On your browser, go to http://127.0.0.1:5000 to use the app

To close the app:
1. Close the browser tab
2. On the CLI, hit Ctrl + C to end the session

You can now safely close the terminal

Note:
The uploaded images and the output files will be saved to "Web App/uploads" and "Web App/static/outputs" and you can safely delete the content inside these folders.