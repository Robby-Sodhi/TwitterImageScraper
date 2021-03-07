import praw
from tweet import Tweet


class Post():
    def __init__(
    self,
    client_id,
    client_secret,
    user_agent,
    username,
    password,
    subreddit,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    search_query,
    flair_id=None
    ):
        self._reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )
        self._flair_id = flair_id
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._search_query = search_query
        self.tweet = Tweet(consumer_key=self._consumer_key, consumer_secret=self._consumer_secret,access_token=self._access_token,access_token_secret=self._access_token_secret,search_query=self._search_query)
        self.subreddit=subreddit

    def __imagePost(self, message, title):
        submission = self._reddit.subreddit(self.subreddit).submit(title, url=self.tweet.mediaUrl, flair_id=self._flair_id)
        submission.reply(message)

    def randomImagePost(self, message, title):
        if not "has:images" in self._search_query:
            raise ValueError("has:images must be in the search_query")
        self.tweet.randomTweet(type="image")
        message = message.format(**self.__dict__)
        title = title.format(**self.__dict__)
        self.__imagePost(message, title)
