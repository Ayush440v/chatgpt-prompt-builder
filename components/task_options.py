import json
import os

def get_task_options(expertise):
    
    # Returns a list of task options based on the selected expertise.
    # The data is loaded from a JSON file.
    
    # Define the path to the JSON file containing expertise tasks data
    data_file = os.path.join('data', 'expertise_tasks.json')
    
    # Open the JSON file and load its content into a dictionary
    with open(data_file, 'r') as file:
        data = json.load(file)
    
    # Retrieve and return the task options for the given expertise
    # If the expertise is not found, return an empty list
    return data.get(expertise, [])