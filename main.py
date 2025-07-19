import praw
import pandas as pd
import datetime
from config import REDDIT_CONFIG

# --- 1. AUTHENTICATION ---
# Using secure config file
reddit = praw.Reddit(
    client_id=REDDIT_CONFIG['client_id'],
    client_secret=REDDIT_CONFIG['client_secret'],
    user_agent=REDDIT_CONFIG['user_agent']
)

# --- 2. SUBREDDIT AND FETCH DATA ---
subreddit_name = 'dataisbeautiful'
subreddit = reddit.subreddit(subreddit_name)

posts_list = []
comments_list = []

print(f"Scraping from r/{subreddit_name}...")

# Fetch the 50 most recent posts
for post in subreddit.new(limit=50):
    # Extract post data as required [cite: 16]
    posts_list.append({
        'PostID': post.id,
        'Title': post.title,
        'Author': str(post.author),
        'Score': post.score,
        'NumComments': post.num_comments,
        'CreatedUTC': post.created_utc
    })

    # Fetch up to 100 top-level comments for each post
    post.comments.replace_more(limit=0) # Removes "MoreComments" objects
    for comment in post.comments.list()[:100]:
        # Extract comment data as required [cite: 17]
        comments_list.append({
            'CommentID': comment.id,
            'PostID': post.id,
            'Author': str(comment.author),
            'Score': comment.score,
            'Body': comment.body,
            'CreatedUTC': comment.created_utc
        })

print("Scraping complete.")

# Create DataFrames
posts_df = pd.DataFrame(posts_list)
comments_df = pd.DataFrame(comments_list)

# Save to CSV files
posts_df.to_csv('posts.csv', index=False)
comments_df.to_csv('comments.csv', index=False)

print("Data saved to posts.csv and comments.csv")
