import os
import json
import requests

class GitHubAPI:
    def __init__(self, token):
        self.api_url = "https://api.github.com"
        self.token = token
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_followers(self):
        """Get the list of followers for the authenticated user."""
        response = requests.get(f"{self.api_url}/user/followers", headers=self.headers)
        response.raise_for_status()
        return [follower['login'] for follower in response.json()]
    
    def get_user_followers(self, username):
        """Get the list of followers for a specific username."""
        response = requests.get(f"{self.api_url}/users/{username}/followers", headers=self.headers)
        response.raise_for_status()
        return [follower['login'] for follower in response.json()]
    
    def get_user_info(self):
        """Get information about the authenticated user."""
        response = requests.get(f"{self.api_url}/user", headers=self.headers)
        response.raise_for_status()
        return response.json()