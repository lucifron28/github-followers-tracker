import os
from github_api import GitHubAPI
from followers_manager import FollowersManager
from utils import write_log
from dotenv import load_dotenv

def load_env_variables():
    from dotenv import load_dotenv
    load_dotenv()

def main():
    load_env_variables()
    
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token not found. Please set it in the .env file.")
    
    github_api = GitHubAPI(token)
    followers_manager = FollowersManager()

    current_followers = github_api.get_followers()
    previous_followers = followers_manager.load_followers()

    added, removed = followers_manager.track_followers(previous_followers, current_followers)

    followers_manager.save_followers(current_followers)
    write_log(added, removed)
    
    print(f"Tracked followers: {len(current_followers)} total, {len(added)} new, {len(removed)} unfollowed")

if __name__ == "__main__":
    main()