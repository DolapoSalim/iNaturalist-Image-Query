import requests
import os
import pandas as pd

# Define species and number of images to download
species_name = "Cystoseira"
num_images = 50  # Adjust as needed
save_folder = "PATH_TO_CREATE_NEW_FOLDER"

# Create folder if not exists
os.makedirs(save_folder, exist_ok=True)

# Search iNaturalist API
url = f"https://api.inaturalist.org/v1/observations?taxon_name={species_name}&per_page={num_images}&order=desc&order_by=created_at"
response = requests.get(url).json()

# Download images
for i, record in enumerate(response['results']):
    if 'photos' in record and record['photos']:
        img_url = record['photos'][0]['url'].replace('square', 'large')  # Get high-res version
        img_data = requests.get(img_url).content
        
        # Save image
        with open(f"{save_folder}/{species_name}_{i}.jpg", "wb") as f:
            f.write(img_data)
        print(f"Downloaded {species_name}_{i}.jpg")

print("Download complete!")