import os
from PIL import Image
import csv

# Define the base folder where images are stored
base_folder = r"C:\mmd assign\Multimodal-Data-Collection\text_data\cleaned"

# CSV file to store metadata
csv_file = os.path.join(base_folder, "..", "images_metadata.csv")  # Saves in 'image_data' directory

# Open CSV file for writing metadata
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(['category', 'filename', 'width', 'height'])
    
    # Iterate through each category folder
    for category in os.listdir(base_folder):
        category_path = os.path.join(base_folder, category)
        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Ensures only images are processed
                    filepath = os.path.join(category_path, filename)
                    try:
                        # Open the image to get its resolution
                        with Image.open(filepath) as img:
                            width, height = img.size
                        # Write row: category, filename, width, height
                        writer.writerow([category, filename, width, height])
                    except Exception as e:
                        print(f"Error processing {filepath}: {e}")

print("Metadata CSV created successfully!")
