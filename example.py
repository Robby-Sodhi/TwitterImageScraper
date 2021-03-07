from post import Post
title = "Source: @{tweet.author} on twitter!"
message = "the tweet URL is {tweet.tweetUrl}, tweet id is {tweet.tweetId}"
test = Post(
client_id="client_id,
client_secret=client_secret,
user_agent="Windows:MyBot:1 (by u/Robstersgaming)",
username=username,
password=password,
subreddit=subreddit,
flair_id=None,
consumer_key=consumer_key,
consumer_secret=consumer_secret,
access_token=access_token,
access_token_secret=access_token_secret,
search_query="SpongeBob has:images"
)

test.randomImagePost(message=message, title=title)
