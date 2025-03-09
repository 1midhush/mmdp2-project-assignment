import os
import pandas as pd

# Folder containing the processed weather CSV files
data_folder = r"C:\mmd assign\Multimodal-Data-Collection\weather_data\processed"

# Function to extract location from file name
def extract_location(filename):
    # Skip the file extension
    name = filename[:-4]  # remove .csv
    # Skip files that are not weather data
    if name.startswith("Station"):
        return None
    
    # If file starts with "weather_", remove the prefix
    if name.startswith("weather_"):
        name = name.replace("weather_", "", 1)
        tokens = name.split("_")
        # Heuristic: use the first token as location if the last token is numeric
        if tokens[-1].isdigit():
            return tokens[0]
        else:
            return tokens[-1]
    
    # For other files, split by underscore
    tokens = name.split("_")
    # If the last token is numeric (likely a year), then use the first token
    if tokens[-1].isdigit():
        return tokens[0]
    else:
        return tokens[-1]

# List to store individual DataFrames
df_list = []

# Process each CSV file in the folder
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        location = extract_location(file)
        if location is None:
            print(f"Skipping file: {file}")
            continue
        
        file_path = os.path.join(data_folder, file)
        try:
            # Read the CSV; sometimes there might be missing values
            df = pd.read_csv(file_path, sep="\t") if "\t" in open(file_path).read(1024) else pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Add a new column for location
        df['location'] = location
        
        # Optionally, convert the time column to datetime (if needed)
        # df['time'] = pd.to_datetime(df['time'], errors='coerce')
        
        # Append to the list
        df_list.append(df)
        print(f"Processed file: {file} with location: {location}")

# Combine all DataFrames into one
if df_list:
    combined_df = pd.concat(df_list, ignore_index=True)
    # Save the combined CSV file in the same folder
    combined_file = os.path.join(data_folder, "combined_weather_data.csv")
    combined_df.to_csv(combined_file, index=False)
    print(f"Combined CSV created successfully at: {combined_file}")
else:
    print("No weather data files were processed.")
