import praw
import os
import random

# Initialize Reddit API connection
reddit = praw.Reddit(
    client_id='HtHICiXnB8vdU6UtZjmacQ',
    client_secret='E5qT0rhTvRUWVIVAkaTzijISQl6TtA',
    user_agent='script:TIFUspyder:1.0 (by /u/areojets)'
)

# Subreddits to pull stories from
subreddits = ["tifu", "AskReddit", "TodayILearned", "funny", "entertainment"]

# Function to fetch viral stories
def fetch_viral_posts(subreddit, batch_size=10, min_upvotes=5000, min_comments=500):
    try:
        # Get top posts sorted by 'top' and 'hot'
        top_posts = list(reddit.subreddit(subreddit).top(time_filter="year", limit=batch_size * 2))
        hot_posts = list(reddit.subreddit(subreddit).hot(limit=batch_size * 2))

        # Combine and filter posts based on upvotes and comments
        posts = top_posts + hot_posts
        viral_posts = [
            p for p in posts 
            if p.selftext and len(p.selftext) < 1500 and p.score >= min_upvotes and p.num_comments >= min_comments
        ]

        # Sample posts if there are more than needed
        if len(viral_posts) > batch_size:
            viral_posts = random.sample(viral_posts, batch_size)

        return viral_posts

    except Exception as e:
        print(f"Error fetching posts: {e}")
        return []

# Function to save each post to a text file
def save_post_to_file(post, index, subreddit):
    os.makedirs("viral_posts", exist_ok=True)
    filename = f"viral_posts/{index}_{subreddit}_{post.id}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Title: {post.title}\n")
        file.write(f"Upvotes: {post.score}\n")
        file.write(f"Comments: {post.num_comments}\n")
        file.write(f"URL: {post.url}\n\n")
        file.write(f"Content:\n{post.selftext}")
    print(f"Post saved to {filename}")

# Main function to process viral posts from multiple subreddits
def batch_process_viral_posts(batch_size=10):
    for subreddit in subreddits:
        print(f"\nFetching viral posts from r/{subreddit}...")
        posts = fetch_viral_posts(subreddit, batch_size=batch_size)
        
        if not posts:
            print(f"No viral posts available to process from r/{subreddit}.")
            continue

        for index, post in enumerate(posts, start=1):
            save_post_to_file(post, index, subreddit)

# Run the batch processing
batch_process_viral_posts(batch_size=10)
