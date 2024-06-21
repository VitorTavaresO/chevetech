import json

screen_manager = None

with open('data.json', 'r+') as file:
            data = json.load(file)

def read_from_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data[0]

def write_to_data(**kwargs):
    with open('data.json', 'r+') as file:
        data = json.load(file)
        data = data[0]

        for key, value in kwargs.items():
            if key.startswith('hotspot_'):
                field_name = key.split('hotspot_')[1]
                if field_name in data['settings_screen']['hotspot']:
                    data['settings_screen']['hotspot'][field_name] = value
                else:
                    print(f"Warning: '{field_name}' is not a valid field for 'hotspot'")
            elif key.startswith('connections_'):
                field_name = key.split('connections_')[1]
                if field_name in data['settings_screen']['connections']:
                    data['settings_screen']['connections'][field_name] = value
                else:
                    print(f"Warning: '{field_name}' is not a valid field for 'connections'")

        file.seek(0)
        json.dump([data], file, indent=4)
        file.truncate()