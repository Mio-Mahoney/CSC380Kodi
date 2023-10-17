import json

profiles_file_path = 'UserData/profiles.json'
current_config_file_path = 'UserData/current_config.json'

profiles_file = open(profiles_file_path, "r+")
current_config_file = open(current_config_file_path, "r+")
profiles_data = json.load(profiles_file)
current_config_data = json.load(current_config_file)

#Adds a profile to profiles.json
def add_profile(profile_dict):
    global profiles_data, profiles_file
    profiles_data.append(profile_dict)
    with open(profiles_file_path, 'w') as json_file:
            json.dump(profiles_data, json_file, indent=4)
    profiles_file = open(profiles_file_path, "r+")
    profiles_data = json.load(profiles_file)

#Deletes a profile from profiles.json
def delete_profile(config_name):
    global profiles_data, profiles_file
    for profile in profiles_data:
        if profile.get("name") == config_name:
            profiles_data.remove(profile)
    with open(profiles_file_path, 'w') as json_file:
            json.dump(profiles_data, json_file, indent=4)
    profiles_file = open(profiles_file_path, "r+")
    profiles_data = json.load(profiles_file)

#Updates the current config being used and writes it to current_config.json
def update_current_config(config_name):
    global current_config_data, current_config_file
    config_to_update = {}
    name_exists = False
    for profile in profiles_data:
        if profile.get("name") == config_name:
            config_to_update = profile
            name_exists = True
            break
    if name_exists:
        with open(current_config_file_path, 'w') as json_file:
            json.dump(config_to_update, json_file, indent=4)
    else:
        pass
    current_config_file = open(current_config_file_path, "r+")
    current_config_data = json.load(current_config_file)





# -----------------------------------------------------------------------------------------------------
# Unfinished Functions
# -----------------------------------------------------------------------------------------------------

# This function will read the files in UserData and put it in the user configuration data arrays
def read_current_configuration():
    pass

# This function will obtain the names of all of the user profiles from our UserData json files
def get_profile_names():
    return ["Harley", "Mio", "Will"]

# This function will save a user's profile to our UserData json files
def add_profile(profile_name):
    pass
