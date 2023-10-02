from configuration import Configuration

class Profiles:
    def __init__(self, profile_list, current_config):
        self.profile_list = profile_list
        self.current_config = current_config
    
        def add_profile(self, profile):
            self.profile_list.append(profile)
        
        def delete_profile(self, profile):
            if profile in self.profile_list:
                self.profile_list.remove(profile)
