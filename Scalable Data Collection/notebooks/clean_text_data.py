import os
import re
from bs4 import BeautifulSoup

# Define raw and cleaned text folders (adjust the paths if needed)
raw_folder = r"C:\mmd assign\Multimodal-Data-Collection\text_data\raw"
cleaned_folder = r"C:\mmd assign\Multimodal-Data-Collection\text_data\cleaned"

# Create the cleaned folder structure if it doesn't exist
os.makedirs(cleaned_folder, exist_ok=True)

# Iterate through each category folder in the raw data
for category in os.listdir(raw_folder):
    raw_category_path = os.path.join(raw_folder, category)
    cleaned_category_path = os.path.join(cleaned_folder, category)
    os.makedirs(cleaned_category_path, exist_ok=True)
    
    if os.path.isdir(raw_category_path):
        for filename in os.listdir(raw_category_path):
            # Process only .html and .txt files
            if filename.lower().endswith(('.html', '.txt')):
                raw_file_path = os.path.join(raw_category_path, filename)
                
                with open(raw_file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                
                # Remove HTML tags using BeautifulSoup (if applicable)
                soup = BeautifulSoup(content, "html.parser")
                text = soup.get_text(separator=" ", strip=True)
                
                # Remove punctuation and digits (optional, adjust regex as needed)
                text = re.sub(r'[^a-zA-Z\s]', '', text)
                text = text.lower()  # Convert to lowercase
                
                # Save the cleaned text to the corresponding folder
                cleaned_file_path = os.path.join(cleaned_category_path, filename)
                with open(cleaned_file_path, 'w', encoding='utf-8') as file:
                    file.write(text)
                
                print(f"Cleaned {raw_file_path} and saved to {cleaned_file_path}")

print("All files cleaned successfully!")
