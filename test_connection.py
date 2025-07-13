# test_connection.py

import praw       # Full form: Python Reddit API Wrapper
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read credentials from environment
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def test_reddit_user(username):
    try:
        redditor = reddit.redditor(username)

        print(f"✅ Fetching data for user: {username}")
        print(f"🗨️  Recent Comments:")

        for comment in redditor.comments.new(limit=3):
            print(f"- {comment.body[:80]}...")

        print(f"\n📝 Recent Posts:")

        for post in redditor.submissions.new(limit=3):
            print(f"- {post.title[:80]}...")

    except Exception as e:
        print("❌ Error:", e)

# Test with sample user
test_reddit_user("noah_bd")
