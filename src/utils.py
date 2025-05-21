import json
from datetime import datetime

def read_json_file(filepath):
    """Read a JSON file and return its contents."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def write_json_file(filepath, data):
    """Write data to a JSON file."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def append_to_markdown_log(log_filepath, entry):
    """Append a new entry to the markdown log."""
    with open(log_filepath, 'a') as log_file:
        log_file.write(entry + '\n')

def format_follower_change(username, action):
    """Format the follower change entry for the markdown log."""
    return f"- {action}: {username} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def write_log(added, removed):
    """Write follower changes to the log file."""
    from followers_manager import LOG_FILE
    
    with open(LOG_FILE, 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if added:
            log_file.write(f"\n## New followers - {timestamp}\n")
            for username in added:
                log_file.write(f"- {username}\n")
        if removed:
            log_file.write(f"\n## Unfollowed - {timestamp}\n")
            for username in removed:
                log_file.write(f"- {username}\n")