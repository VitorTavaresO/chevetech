import json

screen_manager = None

with open('data.json', 'r') as file:
            data = json.load(file)

data = data[0]