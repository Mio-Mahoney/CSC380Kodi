import xbmc
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
dialog = xbmcgui.Dialog()
window = xbmcgui.Window()

def display_random_button():
    user_choice = dialog.yesnocustom("Kodi Episode Picker", "What would you like to do?", "", "Configuration", "Random Select")
    if user_choice:
        dialog.ok("Kodi Episode Picker","This is where our randomization will occur")
    else:
        display_configuration_page()

def display_configuration_page():
    # Arrays that hold possible choices for the different configurations
    genres = ["Any","Action", "Comedy", "Drama", "Horror", "Science Fiction"]
    lengths = ["Any", "0-30 Minutes", "31-60 minutes", "61-90 minutes","91-120 minutes","121-180 minutes",">180 minutes",]

    genre_labels = [f"{genre}" for genre in genres]
    length_labels = [f"{length}" for length in lengths]
     
    # Create a multiselect list for genres
    genre_choice = dialog.multiselect("Select Movie Genres", genre_labels)
    
    # Create a yes/no control for watched/unwatched
    watched_unwatched_choice = dialog.yesnocustom("Kodi Episode Picker", "Do you want to see media you've already watched?", "Unwatched", "Watched", "Any")
    
    # Create a select control for movie length
    length_choice = dialog.multiselect("Select Movie Length", length_labels)


display_random_button()





