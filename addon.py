import xbmc
import xbmcaddon
import xbmcgui

from src import json_utils

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
dialog = xbmcgui.Dialog()
window = xbmcgui.Window()

# User configuration data that will be used throughout the program
genre_choice = []
watched_unwatched_choice = []
length_choice = []
rating_choice = []
mood_choice = []

# Displays main page where the user can choose to randomly select, configure, or choose profile
def display_random_button():
    # user_choice is assigned based on the user's choice. 
    # 0 : Configuration
    # 1 : Random Select
    # 2 : Choose Profile
    user_choice = dialog.yesnocustom("Kodi Episode Picker", "What would you like to do?", "Choose Profile", "Configuration", "Random Select")
    if user_choice == 0:
        display_configuration_page()
    elif user_choice == 1:
        config = json_utils.current_config_data
        user_choice = dialog.yesno("Kodi Episode Picker", "Would you like to choose media based on your mood today?")
        if user_choice:
            display_mood_page()
        else:
            play_random_media(config)
    else:
        display_profile_page()
        

# Displays a page where the user can choose what profile they want to use
def display_profile_page():
    profile_names = json_utils.get_profile_names()
    profile_labels = [f"{profile}" for profile in profile_names]
    profile_choice_num = [dialog.select("Select Profile you want to use", profile_labels)]
    profile_choice = convert_indexes_to_strings(profile_choice_num, profile_labels)[0]
    json_utils.update_current_config(profile_choice)
    dialog.ok("Kodi Episode Picker", f"Your random play button is now configured to {profile_choice}!")


def display_configuration_page():
    # Arrays that hold possible choices for the different configurations
    genres = ["Action", "Comedy", "Drama", "Horror", "Science Fiction"]
    lengths = ["0-30 Minutes", "31-60 minutes", "61-90 minutes","91-120 minutes","121-180 minutes",">180 minutes",]
    ratings = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"]

    genre_labels = [f"{genre}" for genre in genres]
    length_labels = [f"{length}" for length in lengths]
    rating_labels = [f"{rating}" for rating in ratings]

    # Controls for user to input configurations
    watched_unwatched_choice = dialog.yesnocustom("Kodi Episode Picker", "Do you want to see media you've already watched?", "Unwatched", "Any", "Watched")
    genre_choice_nums = dialog.multiselect("Select Movie Genres", genre_labels)
    genre_choice = convert_indexes_to_strings(genre_choice_nums, genre_labels)
    length_choice_nums = dialog.multiselect("Select Movie Length", length_labels)
    length_choice = convert_indexes_to_strings(length_choice_nums, length_labels)
    rating_choice_nums = dialog.multiselect("Select Movie Rating", rating_labels)
    rating_choice = convert_indexes_to_strings(rating_choice_nums, rating_labels)

    # Controls for user to save configuration as profile
    save_as_profile = dialog.yesno("Kodi Episode Picker", "Would you like to save this configuration as a profile?")
    if(save_as_profile):
        profile_name = dialog.input("What do you want the name of the profile to be?")
        profile_dict = create_profile_dict()
        json_utils.add_profile(profile_dict)
    else:
        dialog.ok("Kodi Episode Picker","Your configuration is now ready to play random media!")

# This function takes the indices that the multiselect controls produce and fills 
# them with the corresponding strings. This will make it much easier to program with
# (Example: the index 0 will instead be "Science Fiction" in genre_choice variable)
def convert_indexes_to_strings(int_arr, string_arr):
    result_arr = []
    for index in int_arr:
        result_arr.append(string_arr[index])
    return result_arr





# -----------------------------------------------------------------------------------------------------
# Unfinished Functions
# -----------------------------------------------------------------------------------------------------

# This function will display the mood page
def display_mood_page():
    dialog.ok("Kodi Episode Picker","This is where our mood page will go.")

# This function will use the user configuration data arrays to randomly choose from media
def play_random_media(config):
    dialog.ok("Kodi Episode Picker","This is where our app will randomly play a movie.")

def create_profile_dict():
    pass

# -----------------------------------------------------------------------------------------------------
# Starts Program
# -----------------------------------------------------------------------------------------------------

display_random_button()







