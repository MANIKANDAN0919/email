import os
import shutil

source_folder = "source_images"
destination_folder = "jpg_images"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Move all .jpg files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )

print("All JPG files moved successfully!")
