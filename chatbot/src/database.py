import os
import json

def load_data(file_name):
    # Get the path relative to the current directory and 'data' folder
    file_path = os.path.join(os.path.dirname(__file__), '../data', file_name)
    
    # Open and load the JSON file with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data
