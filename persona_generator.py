import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


# 🔑 Load Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("API key not found!")


# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def build_prompt(user_data):
    """
    Converts Reddit user data into a prompt.
    """
    prompt = "You are an AI that builds user personas from Reddit activity.\n"
    prompt += "Based on the following posts and comments, create a detailed user persona. Include personality, interests, values, and communication style. Add citations (permalinks).\n\n"

    for item in user_data:
        if item["type"] == "post":
            prompt += f"[POST]\nTitle: {item['title']}\nText: {item['text']}\nSubreddit: {item['subreddit']}\nLink: {item['permalink']}\n\n"
        elif item["type"] == "comment":
            prompt += f"[COMMENT]\nText: {item['text']}\nSubreddit: {item['subreddit']}\nLink: {item['permalink']}\n\n"

    prompt += "Return the persona in structured format with citation links."
    return prompt

def generate_persona(user_data):
    prompt = build_prompt(user_data)

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Gemini API error:", e)
        return None

