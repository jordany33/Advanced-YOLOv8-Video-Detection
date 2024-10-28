# Object Detection using YOLO

This project provides an easy-to-use implementation for detecting objects in videos using the YOLO (You Only Look Once) model.

## Features
- Supports multiple video formats including `.mp4`, `.avi`, `.flv`, `.mkv`, and `.mov`.
- Organized code structure with clear separation of concerns.
- Logs detection results to a dedicated folder.
- Progress bar for video processing.
- Error handling for video processing.

## Prerequisites
- Python 3.x
- OpenCV
- Ultralytics YOLO

## Getting Started
1. **Clone the Repository**:
\`\`\`
git clone https://github.com/jordany33/Advanced-YOLOv8-Video-Detection.git
cd Advanced-YOLOv8-Video_Detection
\`\`\`

2. **Install Dependencies**:
\`\`\`
pip install -r requirements.txt
\`\`\`

3. **Run the Object Detector**:
\`\`\`
python main.py
\`\`\`

## Directory Structure
- `object_detector.py`: Contains the main class for object detection.
- `main.py`: Entry point of the program.
- `utils.py`: Utility functions for the project.
- `logs/`: Folder where the detection results are saved.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
