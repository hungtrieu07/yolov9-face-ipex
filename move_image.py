import os
import shutil
from tqdm import tqdm

def move_images_to_single_folder(source_dir, destination_dir):
    # Count the total number of files to process
    total_files = sum(len(files) for _, _, files in os.walk(source_dir))

    # Initialize tqdm progress bar
    progress_bar = tqdm(total=total_files, desc='Moving Images')

    # Iterate through all files and directories in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file is an image (you may extend this check based on your specific needs)
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Construct the source path for the file
                source_path = os.path.join(root, file)
                try:
                    # Construct the destination path for the file
                    destination_path = os.path.join(destination_dir, file)
                    # Move the file to the destination directory
                    shutil.move(source_path, destination_path)
                    # Update the progress bar
                    progress_bar.update(1)
                except Exception as e:
                    print(f"Error moving {source_path}: {e}")

    # Close tqdm progress bar
    progress_bar.close()

# Specify the source directory containing subfolders with images
source_directory = '/mnt/e/WIDER_val/WIDER_val/images'

# Specify the destination directory where all images will be moved
destination_directory = '/mnt/e/face_val'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Call the function to move images to a single folder
move_images_to_single_folder(source_directory, destination_directory)
