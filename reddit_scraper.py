python
import praw
import os

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="user_persona_script"
    )

def extract_username(url):
    return url.strip("/").split("/")[-1]

def fetch_user_data(username):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=20):
        posts.append(f"[POST] {post.title}: {post.selftext}")

    for comment in user.comments.new(limit=20):
        comments.append(f"[COMMENT] {comment.body}")

    return posts + comments