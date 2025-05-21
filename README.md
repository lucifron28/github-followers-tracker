# GitHub Followers Tracker

This project tracks who follows and unfollows your GitHub account. It utilizes the GitHub API to fetch follower data and logs changes in a markdown file. The tracking process is automated using GitHub Actions, which runs the script on commits associated with your name and email.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Generating a Personal Access Token](#generating-a-personal-access-token)
- [Environment Variables](#environment-variables)
- [GitHub Actions](#github-actions)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/github-followers-tracker.git
   cd github-followers-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Copy the `.env.example` file to `.env` and fill in your GitHub personal access token:
   ```
   cp .env.example .env
   ```

## Usage

To run the script manually, execute the following command:
```
python src/main.py
```

The script will fetch your current followers and compare them with the previous list stored in `data/followers.json`. It will log any changes in `logs/followers_log.md`.

## Generating a Personal Access Token

1. Go to your GitHub account settings.
2. Navigate to **Developer settings** > **Personal access tokens**.
3. Click on **Generate new token**.
4. Select the scopes you need (for this project, you will need `read:user`).
5. Copy the generated token and store it securely.

## Environment Variables

The project requires the following environment variable to be set in the `.env` file:

```
GITHUB_TOKEN=your_personal_access_token
```

## GitHub Actions

The project includes a GitHub Actions workflow defined in `.github/workflows/track-followers.yml`. This workflow is triggered on commits associated with your name and email, automating the tracking process.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.