import json
import os

def get_expertise_options(domain):
    
    # Returns a list of expertise options based on the selected domain.
    # The data is loaded from a JSON file.
    
    # Define the path to the JSON file containing domain expertise data
    data_file = os.path.join('data', 'domain_expertise.json')
    
    # Open the JSON file and load its content into a dictionary
    with open(data_file, 'r') as file:
        data = json.load(file)
    
    # Retrieve and return the expertise options for the given domain
    # If the domain is not found, return an empty list
    return data.get(domain, [])