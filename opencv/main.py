import argparse
from object_detector import ObjectDetector

def main(model_path, video_folder, show_detection=True):
    object_detector = ObjectDetector(model_path, video_folder, show_detection)
    object_detector.process_videos()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the object detector on a folder of videos.")
    parser.add_argument('--model_path', type=str, default='yolov8n.pt', help='Path to the YOLO model.')
    parser.add_argument('--video_folder', type=str, required=True, help='Path to the folder containing videos.')
    parser.add_argument('--show_detection', type=bool, default=True, help='Whether or not to show detection results.')

    args = parser.parse_args()
    
    main(args.model_path, args.video_folder, args.show_detection)
