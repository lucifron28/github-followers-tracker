import os
from github_api import GitHubAPI
from followers_manager import FollowersManager
from utils import write_log

def load_env_variables():
    """Load environment variables from .env file if present (for local development)"""
    try:
        from dotenv import load_dotenv
        if os.path.exists('.env'):
            load_dotenv()
    except ImportError:
        pass

def main():
    load_env_variables()
    
    token = os.environ.get('PERSONAL_ACCESS_TOKEN') or os.environ.get('GITHUB_TOKEN')
    
    if not token:
        raise ValueError("GitHub token not found. Please set it as PERSONAL_ACCESS_TOKEN or GITHUB_TOKEN in environment variables.")

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