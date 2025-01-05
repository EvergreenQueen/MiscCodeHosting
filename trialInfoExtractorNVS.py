import os
import re
import json

# Define the folder path
folder_path = r"C:\code\BGC\NaturalisticVisualSearchTask\NVS Version A\Stimulus"

# Initialize an empty list to store the JSON objects
json_objects = []

# Regular expression pattern to match filenames like "O_101E_DxO.png"
pattern =  r'O_([0-9]+)([A-Z]+)_DxO.png'

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    match = re.match(pattern, filename)
    
    if match:
        target_id, target_present_str = match.groups()
        target_type = target_present_str or 'unknown'
        id = target_id or 'unknown'
        
        # Create the "presentation" dictionary
        presentation = {
            "type": ["image"],
            "id" : id + match.group(2),
            "sequence": [
                {
                    "type" : ["image"],
                    "id" : id + match.group(2),
                    "timing-id" : "stimuli-image"
                },
                {
                    "type" : ["image"],
                    "id" : match.group(1) + "T",
                    "timing-id" : "target-image"
                }
            ]
        }

        response = {}
        
        #target present
        if target_type == "E" or target_type == "U":

            # Create the "response" dictionary with choices
            response = {
                "type": "keyboard_input",
                "keyChoices": [
                    {"key": "p" , "id": "P", "correct": True},
                    {"key": "a" , "id": "A"}
                ]
            }
        elif target_type == "L" : #not present
            response = {
                "type": "keyboard_input",
                "keyChoices": [
                    {"key" : "p", "id": "P"},
                    {"key" : "a", "id": "A", "correct": True}
                ]
            }
        
        # Create the final JSON object
        json_object = {
            "presentation": presentation,
            "response": response
        }
        
        json_objects.append(json_object)

# Create a JSON file to store the results
output_filename = 'trialOutput.json'
with open(output_filename, 'w') as output_file:
    json.dump(json_objects, output_file, indent=4)

print(f'JSON objects have been saved to {output_filename}')
