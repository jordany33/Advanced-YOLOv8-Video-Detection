# Object Detection with YOLOv8

This project uses the YOLO (You Only Look Once) algorithm, specifically YOLOv8, to perform object detection on video files. It utilizes the Ultralytics' YOLO implementation. The code detects objects frame by frame in each video and outputs the total number of objects detected. It also gives the option to visualize the detection results. Finally, it saves the detected objects and their details to a text file.

## Dependencies

- `cv2`: OpenCV for reading and processing video files
- `os`: Standard Python library for OS dependent functionalities
- `ultralytics.yolo.v8`: Ultralytics' implementation of YOLOv8 for object detection

To install these dependencies, you can use pip:

```bash
pip install opencv-python
pip install ultralytics
