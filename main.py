python
import sys
from reddit_scraper import extract_username, fetch_user_data
from persona_builder import build_persona
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_profile_url>")
        return

    url = sys.argv[1]
    username = extract_username(url)
    print(f"Fetching data for: {username}")

    data = fetch_user_data(username)
    persona = build_persona(data, username)

    os.makedirs("data", exist_ok=True)
    with open(f"data/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to data/{username}_persona.txt")

if __name__ == "__main__":
    main()
