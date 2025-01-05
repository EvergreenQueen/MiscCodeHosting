import os
import re
import json

# Define the folder path
folder_path = r"C:\code\BGC\NaturalisticVisualSearchSSR_Compressed\NVS Version A\Stimulus"
target_folder_path =  r"C:\code\BGC\NaturalisticVisualSearchTask\NVS Version A\Targets"


# Initialize an empty list to store the JSON objects
json_objects = []

#Putting all targets as their own resource
target_pattern = r'TO_([0-9]+)_(.*).png'

for filename in os.listdir(target_folder_path):
    match = re.match(target_pattern, filename)

    if match:
        id = match.group(1)
        json_object = {
            "id" : id + "T",
            "type": "image",
            "file": filename
        }

        json_objects.append(json_object)




# Regular expression pattern to match filenames like "O_<number><letter>_DxO.png" | "ba_normalized_av_50.wmv"
pattern = r'O_([0-9]+)([A-Z]+)_DxO.jpg'

#Counter:
count = 0

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    # print(f"Looking at: {filename}")
    match = re.match(pattern, filename)
    
    if match:
        # print("found a match")
        target_id, target_present_str = match.groups()
        target_type = target_present_str or 'unknown'
        trial_id = f"NVS_{count}"
        
        # Create a dictionary for the JSON object
        json_object = {
            "id": target_id + match.group(2),
            "type": "image",
            "file": filename,
            "targetStatus": target_type,
            "trialID": trial_id
        }
        count += 1
        
        json_objects.append(json_object)
        print(json_object)

# Create a JSON file to store the results
output_filename = 'resourceOutput.json'
with open(output_filename, 'w') as output_file:
    json.dump(json_objects, output_file, indent=4)

print(f'JSON objects have been saved to {output_filename}')


