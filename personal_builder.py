python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_persona(posts_and_comments, username):
    content = "\n".join(posts_and_comments)
    prompt = (
        f"Based on the following Reddit posts and comments from user {username}, "
        "generate a detailed user persona. Include details like age, occupation, hobbies, beliefs, tone, writing style, etc. "
        "Cite specific quotes to justify each characteristic.\n\n"
        f"{content}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )

    return response['choices'][0]['message']['content'],

