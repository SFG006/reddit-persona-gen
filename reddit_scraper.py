# reddit_scraper.py

import praw                     # Import Reddit API wrapper
import os                       # To access environment variables
from dotenv import load_dotenv # To load .env file

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Create Reddit instance using PRAW
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

def extract_username_from_url(profile_url):
    """
    Takes Reddit profile URL and extracts the username.
    Example: 'https://www.reddit.com/user/kojied/' → 'kojied'
    """
    return profile_url.rstrip('/').split('/')[-1]

def scrape_reddit_user(profile_url, limit=50):
    """
    Scrapes a Reddit user's recent posts and comments.
    Returns a list of dictionaries with content and type.
    """
    username = extract_username_from_url(profile_url)
    redditor = reddit.redditor(username)

    user_data = []

    # Scrape latest submissions (posts)
    for submission in redditor.submissions.new(limit=limit):
        user_data.append({
            "type": "post",
            "title": submission.title,
            "text": submission.selftext,
            "subreddit": str(submission.subreddit),
            "url": submission.url,
            "permalink": f"https://www.reddit.com{submission.permalink}"
        })

    # Scrape latest comments
    for comment in redditor.comments.new(limit=limit):
        user_data.append({
            "type": "comment",
            "text": comment.body,
            "subreddit": str(comment.subreddit),
            "permalink": f"https://www.reddit.com{comment.permalink}"
        })

    return user_data
