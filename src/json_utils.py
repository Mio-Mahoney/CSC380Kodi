import json
import xbmcvfs

root_path = xbmcvfs.translatePath("special://xbmc/addons/script.episode.picker") + "\\UserData\\"
presets_file_path = root_path+'presets.json'
current_config_file_path = root_path+'current_config.json'

presets_file = open(presets_file_path, "r+")
current_config_file = open(current_config_file_path, "r+")
presets_data = json.load(presets_file)
current_config_data = json.load(current_config_file)

#Adds a preset to presets.json
def add_preset(preset_dict):
    global presets_data, presets_file
    presets_data.append(preset_dict)
    with open(presets_file_path, 'w') as json_file:
            json.dump(presets_data, json_file, indent=4)
    presets_file = open(presets_file_path, "r+")
    presets_data = json.load(presets_file)

#Deletes a preset from presets.json
def delete_preset(config_name):
    global presets_data, presets_file
    for preset in presets_data:
        if preset.get("name") == config_name:
            presets_data.remove(preset)
    with open(presets_file_path, 'w') as json_file:
            json.dump(presets_data, json_file, indent=4)
    presets_file = open(presets_file_path, "r+")
    presets_data = json.load(presets_file)

#Updates the current config being used and writes it to current_config.json
def update_current_config(config_name):
    global current_config_data, current_config_file
    config_to_update = {}
    name_exists = False
    for preset in presets_data:
        if preset.get("name") == config_name:
            config_to_update = preset
            name_exists = True
            break
    if name_exists:
        with open(current_config_file_path, 'w') as json_file:
            json.dump(config_to_update, json_file, indent=4)
    else:
        pass
    current_config_file = open(current_config_file_path, "r+")
    current_config_data = json.load(current_config_file)

# This function will obtain the names of all of the user presets from our UserData json files
def get_preset_names():
    global presets_data
    names = []
    for item in presets_data:
        names.append(item["name"])
    return names





# -----------------------------------------------------------------------------------------------------
# Unfinished Functions
# -----------------------------------------------------------------------------------------------------

# This function will save a user's preset to our UserData json files
def add_preset(preset_name):
    pass
