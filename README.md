# Reddit_Assignment

# Reddit User Persona Builder

## 🚀 Description
This tool scrapes a Reddit user's posts and comments, then uses an LLM (GPT-4) to generate a detailed user persona with citations.

## 🔧 Requirements
- Python 3.8+
- Reddit API credentials
- OpenAI API key

## 📦 Installation

bash
pip install -r requirements.txt
`

Create a `.env` file (or set as environment variables):


REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
OPENAI_API_KEY=your_openai_key


## ✅ Usage

bash
python main.py https://www.reddit.com/user/kojied/


The output will be saved in the `data/` directory.

## 📁 Output Example

* `data/kojied_persona.txt` - contains the persona and quoted sources.



---

### 📦 requirements.txt



praw
openai
python-dotenv

`

---

## 📝 Sample Output (kojied_persona.txt)

txt
👤 Reddit User Persona: kojied

• Age: Likely in their 20s based on pop culture references and gaming discussions.

• Interests:
  - Passionate about video games — cites titles like "Dark Souls" and "Elden Ring".
  - Engages in philosophical debates — one comment reads, “What is even the point of free will if everything is predetermined?”

• Writing Style:
  - Reflective and analytical; frequent use of introspective language.

• Personality Traits:
  - Curious and articulate.
  - Open-minded — debates civilly and acknowledges opposing views.

Sources:
- [COMMENT] “What is even the point of free will if everything is predetermined?”
- [POST] “Started Elden Ring again, trying faith build this time. Let’s see how it goes.”
...
`

---

## 📌 Submission Instructions

Push all above files to a *public GitHub repository* and share the link on Internshala.
