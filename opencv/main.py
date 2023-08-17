from object_detector import ObjectDetector

if __name__ == "__main__":
    # Run the object detector
    object_detector = ObjectDetector('yolov8n.pt', '/path/to/your/videos/folder', show_detection=True)
    object_detector.process_videos()
