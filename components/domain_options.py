import json
import os

def get_domain_options():
    
    # Returns a list of domain options for the user to select.
    # The data is loaded from a JSON file.
    
    # Define the path to the JSON file containing domain expertise data
    data_file = os.path.join('data', 'domain_expertise.json')
    
    # Open the JSON file and load its content into a dictionary
    with open(data_file, 'r') as file:
        data = json.load(file)
    
    # Return the keys of the dictionary as a list, representing domain options
    return list(data.keys())