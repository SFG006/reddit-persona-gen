```markdown
# Reddit User Persona Generator 🤖

This project generates a detailed user persona by analyzing Reddit posts and comments from a given profile URL. It scrapes public data using Reddit's API and summarizes the user's personality, interests, and values using Gemini Pro (Google Generative AI).

---

## 🚀 Features

- 🔍 Scrapes posts & comments from any Reddit user
- 🧠 Generates structured user persona using Gemini (LLM)
- 🔗 Includes citations to original Reddit content
- 📝 Saves output as a `.txt` file

---

## 📁 Project Structure

```

reddit-persona-gen/
├── main.py                    # Entry point script
├── reddit\_scraper.py          # Scrapes Reddit user data
├── persona\_generator.py       # Builds prompt & sends to Gemini
├── utils.py                   # Handles file output
├── requirements.txt           # Required Python packages
├── .env                       # API keys (not included in repo)
└── output/
├── persona\_ChiefLeef22.txt
└── persona\_noah_bd.txt
└── persona\_zardvark.txt
└── notebook.ipynb

````

---

## 🧩 Technologies Used

- 🐍 Python 3.8+
- [`praw`](https://praw.readthedocs.io/) – Reddit API Wrapper
- [`google-generativeai`](https://github.com/google/generative-ai-python) – Gemini API
- `python-dotenv` – Load API keys from `.env`

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/reddit-persona-gen.git
   cd reddit-persona-gen
````

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file:**

   ```
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=your_app_user_agent
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the script:**

   ```bash
   python main.py https://www.reddit.com/user/ChiefLeef22/
   ```

5. **Output will be saved to:**

   ```
   output/persona_ChiefLeef22.txt
   ```

---

## 📌 Example Profiles (Required by Assignment)

* [`u/ChiefLeef22`](https://www.reddit.com/user/ChiefLeef22/)
* [`u/noah_bd`](https://www.reddit.com/user/noah_bd/)
* [`u/zardvark`](https://www.reddit.com/user/zardvark/)

Output for both is included in the `/output` folder.

---

## ✅ Notes

* LLM output may vary slightly based on context length and API model.
* Only public Reddit data is used.
* You can modify the limit of posts/comments using:

  ```bash
  python main.py <url> --limit 30
  ```

---

---

## 📓 Bonus: Development Notebook

This repository also contains `notebook.ipynb`, where initial tests and ideas were explored before building the final modular scripts. You can open it to see how logic was developed and verified.

---

## 📬 Author

Made by SFG006

---
