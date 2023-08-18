import os
from tqdm import tqdm

def get_video_files(folder_path):
    video_extensions = ['.mp4', '.avi', '.flv', '.mkv', '.mov']
    video_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1] in video_extensions]
    return video_files

def save_results_to_file(results, video_file, log_folder):
    result_file = os.path.join(log_folder, f'{os.path.splitext(video_file)[0]}_results.txt')
    with open(result_file, 'w') as file:
        for result in tqdm(results, desc="Saving results"):
            # This assumes result can be converted to string directly. Modify if not the case.
            file.write(str(result) + '\n')
