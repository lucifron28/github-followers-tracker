import json
import os
from datetime import datetime

FOLLOWERS_FILE = os.path.join(os.path.dirname(__file__), '../data/followers.json')
LOG_FILE = os.path.join(os.path.dirname(__file__), '../logs/followers_log.md')

class FollowersManager:
    def __init__(self):
        self.followers_file = FOLLOWERS_FILE
        self.log_file = LOG_FILE
    
    def load_followers(self):
        """Load the list of followers from the JSON file."""
        if not os.path.exists(self.followers_file):
            return []
        
        with open(self.followers_file, 'r') as file:
            data = json.load(file)
            # Handle both possible formats
            if isinstance(data, list):
                return data
            elif 'followers' in data:
                return data.get('followers', [])
            return []
    
    def save_followers(self, followers):
        """Save the list of followers to the JSON file."""
        with open(self.followers_file, 'w') as file:
            json.dump({"followers": followers}, file, indent=2)
    
    def track_followers(self, previous_followers, current_followers):
        """Track changes in followers."""
        current_set = set(current_followers)
        previous_set = set(previous_followers)
        
        new_followers = current_set - previous_set
        unfollowed = previous_set - current_set
        
        return list(new_followers), list(unfollowed)