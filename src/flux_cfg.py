import json


def load_flux_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
