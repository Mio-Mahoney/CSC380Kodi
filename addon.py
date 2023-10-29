import xbmc
import xbmcaddon
import xbmcgui

from src import json_utils

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
dialog = xbmcgui.Dialog()
window = xbmcgui.Window()

# User configuration data that will be used throughout the program
preset_name = ""
watch_status_choice = -1
genre_choice = []
length_choice = []
release_year_choice = []
ratings_choice = []
languages_choice = []
parental_advisory_choice = []
closed_captions_choice = -1

# Displays main page where the user can choose to randomly select, configure, or choose preset
def display_home_page():
    # user_choice is assigned based on the user's choice. 
    # 0 : Configuration
    # 1 : Random Select
    # 2 : Choose Preset
    user_choice = dialog.yesnocustom("Kodi Episode Picker", "What would you like to do?", "Choose Preset", "Configuration", "Random Select")
    if user_choice == 0:
        display_configuration_page()
    elif user_choice == 1:
        config = json_utils.current_config_data
        user_choice = dialog.yesno("Kodi Episode Picker", "Would you like to choose media based on your mood today?")
        if user_choice:
            display_mood_page()
        else:
            play_random_media()
    else:
        display_preset_page()

# Displays a page where the user can choose what preset they want to use
def display_preset_page():
    preset_names = json_utils.get_preset_names()
    preset_labels = [f"{preset}" for preset in preset_names]
    preset_choice_num = [dialog.select("Select preset you want to use", preset_labels)]
    preset_choice = convert_indexes_to_strings(preset_choice_num, preset_labels)[0]
    json_utils.update_current_config(preset_choice)
    dialog.ok("Kodi Episode Picker", f"Your random play button is now configured to {preset_choice}!")

# Displays the configuration home page       
def display_configuration_page():
    reset_config()
    config_choice = dialog.contextmenu(['Watch Status','Genre','Length','Release Year','Rating','Language','Parental Advisory','Closed Captions', 'Save', 'Exit'])
    if config_choice == 0:
        display_watch_status_page()
        display_configuration_page()
    if config_choice == 1:
        display_genre_page()
        display_configuration_page()
    if config_choice == 2:
        display_length_page()
        display_configuration_page()
    if config_choice == 3:
        display_release_year_page()
        display_configuration_page()
    if config_choice == 4:
        display_ratings_page()
        display_configuration_page()
    if config_choice == 5:
        display_languages_page()
        display_configuration_page()
    if config_choice == 6:
        display_parental_advisory_page()
        display_configuration_page()
    if config_choice == 7:
        display_closed_captions_page()
        display_configuration_page()
    if config_choice == 8:
        display_preset_save_page()
        display_home_page()
    if config_choice == 9:
        display_preset_exit_page()
        display_home_page()

def display_mood_page():
    moods = ["Happy", "Sad", "Scary", "Surprising", "Relaxing", "Uplifting"]
    mood_labels = [f"{mood}" for mood in moods]
    mood_choice_nums = dialog.multiselect("Select Movie Genres", mood_labels)
    mood_choice = convert_indexes_to_strings(mood_choice_nums, mood_labels)

# Displays a page where the user can choose if they want to see media they've already seen
def display_watch_status_page():
    watch_status_choice = dialog.yesnocustom("Kodi Episode Picker", "Do you want to see media you've already watched?", "Unwatched", "Any", "Watched")

# Displays a page where the user can choose what genres they want to watch
def display_genre_page():
    genres = ["Action", "Comedy", "Drama", "Horror", "Science Fiction"]
    genre_labels = [f"{genre}" for genre in genres]
    genre_choice_nums = dialog.multiselect("Select Movie Genres", genre_labels)
    genre_choice = convert_indexes_to_strings(genre_choice_nums, genre_labels)

# Displays a page where the user can choose what lengths of media they want to watch
def display_length_page():
    lengths = ["0-30 Minutes", "31-60 minutes", "61-90 minutes","91-120 minutes","121-180 minutes",">180 minutes"]
    length_labels = [f"{length}" for length in lengths]
    length_choice_nums = dialog.multiselect("Select Movie Length", length_labels)
    length_choice = convert_indexes_to_strings(length_choice_nums, length_labels)

# Displays a page where the user can choose what release years they would like to watch
def display_release_year_page():
    years = [str(year) for year in range(1900, 2031)][::-1]
    release_year_choice.append(dialog.select("Choose Minimum Year", years))
    release_year_choice.append(dialog.select("Choose Maximum Year", years))


# Displays a page where the user can choose what ratings they would like to watch
def display_ratings_page():
    ratings = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"]
    rating_labels = [f"{rating}" for rating in ratings]
    rating_choice_nums = dialog.multiselect("Select Movie Ratings", rating_labels)
    rating_choice = convert_indexes_to_strings(rating_choice_nums, rating_labels)

# Displays a page where the user can choose what languages they would like to watch
def display_languages_page():
    languages = ["English", "Spanish", "German", "French", "Mandarin", "Hindi", "Arabic", "Portuguese", "Bengali", "Russian", "Japanese"]
    language_labels = [f"{language}" for language in languages]
    language_choice_nums = dialog.multiselect("Select Movie Languages", language_labels)
    languages_choice_choice = convert_indexes_to_strings(language_choice_nums, language_labels)

# Displays a page where the user can choose what parental advisory ratings they would like to watch
def display_parental_advisory_page():
    parent_ratings = ["G", "PG", "PG-13", "R", "NR"]
    parent_rating_labels = [f"{parent_rating}" for parent_rating in parent_ratings]
    parent_rating_choice_nums = dialog.multiselect("Select Parental Advisory Ratings", parent_rating_labels)
    parental_advisory_choice = convert_indexes_to_strings(parent_rating_choice_nums, parent_rating_labels)

# Displays a page where the user can choose if they want to only watch media with closed captions
def display_closed_captions_page():
    closed_captions_choice = dialog.yesno("Kodi Episode Picker", "Do you want to only watch media with closed captions?")

# Controls for user to save configuration as preset
def display_preset_save_page():
    preset_name = dialog.input("What do you want the name of the preset to be?")
    preset_dict = create_preset_dict()
    json_utils.add_preset(preset_dict)
    reset_config()
    dialog.ok("Kodi Episode Picker","Your configuration is now ready to play random media!")

def display_preset_exit_page():
    user_choice = dialog.yesno("Kodi Episode Picker", "Do you want to stop configuring this preset? Your current configurations won't be saved.")
    if user_choice:
        display_home_page()
    else:
        display_configuration_page()

# This function will use the user configuration data arrays to randomly choose from media
def play_random_media():
    dialog.ok("Kodi Episode Picker","This is where our app will randomly play a movie.")

# This function takes the indices that the multiselect controls produce and fills 
# them with the corresponding strings. This will make it much easier to program with
# (Example: the index 0 will instead be "Science Fiction" in genre_choice variable)
def convert_indexes_to_strings(int_arr, string_arr):
    result_arr = []
    for index in int_arr:
        result_arr.append(string_arr[index])
    return result_arr

def reset_config():
    preset_name = ""
    watch_status_choice = -1
    genre_choice = []
    length_choice = []
    release_year_choice = []
    ratings_choice = []
    languages_choice = []
    parental_advisory_choice = []
    closed_captions_choice = -1

def create_preset_dict():
    return {
        "name": preset_name,
        "watch-status": watch_status_choice,
        "genres": genre_choice,
        "media-length": length_choice,
        "release-year": release_year_choice,
        "ratings": ratings_choice,
        "languages": languages_choice,
        "parental-advisory": parental_advisory_choice,
        "closed-captions": closed_captions_choice
    }

# -----------------------------------------------------------------------------------------------------
# Starts Program
# -----------------------------------------------------------------------------------------------------

display_home_page()
