import os
import cv2
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from utils import get_video_files, save_results_to_file

class ObjectDetector:
    def __init__(self, model_path, videos_folder, show_detection=True, log_folder="logs"):
        self.model = YOLO(model_path)
        self.videos_folder = videos_folder
        self.show_detection = show_detection
        self.log_folder = log_folder
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

    def process_videos(self):
        video_files = get_video_files(self.videos_folder)
        for video_file in video_files:
            video_path = os.path.join(self.videos_folder, video_file)
            try:
                results = self.model.predict(source=video_path, show=self.show_detection)
                print(f'Video: {video_file} - Number of Objects Detected: {len(results)}')
                save_results_to_file(results, video_file, self.log_folder)
            except Exception as e:
                print(f"Error processing {video_file}: {e}")
