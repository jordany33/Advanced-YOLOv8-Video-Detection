import os
from tqdm import tqdm

def get_video_files(folder_path):
    video_extensions = ['.mp4', '.avi', '.flv', '.mkv', '.mov']
    video_files = [f for f in os.listdir(folder_path) if any(f.endswith(ext) for ext in video_extensions)]
    return video_files

def save_results_to_file(results, video_file, log_folder):
    result_file = os.path.join(log_folder, f'{video_file.split(".")[0]}_results.txt')
    with open(result_file, 'w') as file:
        for result in tqdm(results, desc="Saving results"):
            file.write(str(result) + '\n')
