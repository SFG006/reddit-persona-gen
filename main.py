import argparse
from reddit_scraper import scrape_reddit_user, extract_username_from_url
from persona_generator import generate_persona
from utils import save_persona_to_file

def main():
    # CLI argument parser
    parser = argparse.ArgumentParser(description="Generate a Reddit user persona using Gemini AI.")
    parser.add_argument("url", help="Reddit profile URL (e.g., https://www.reddit.com/user/kojied/)")
    parser.add_argument("--limit", type=int, default=50, help="Number of posts/comments to fetch (default: 50)")

    args = parser.parse_args()
    url = args.url
    limit = args.limit

    # Scrape data
    print(f"🔍 Scraping Reddit data from {url}")
    user_data = scrape_reddit_user(url, limit=limit)

    if not user_data:
        print("⚠️ No data found for this user or user doesn't exist.")
        return

    # Generate persona
    print("🧠 Generating persona using Gemini...")
    persona = generate_persona(user_data)

    if persona:
        username = extract_username_from_url(url)
        save_persona_to_file(persona, username)
    else:
        print("❌ Failed to generate persona.")

if __name__ == "__main__":
    main()
