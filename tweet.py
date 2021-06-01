import util

#from fileStuff import readMasterId, isMasterIdEmpty
#from Used import isIdUsed, isAllUsed, appendId
#from writeids import getTwitterIds, today, getLastMasterIdDate
#from parseTweet import getTweetAuthor, getTweetMedia, getTweetText

import tweepy
import random
import tweepy

#EXPECTED_ATTRIBUTES = ['author', 'mediaUrl', 'tweetId']
EXPECTED_ATTRIBUTES = ['tweets','author','mediaUrl','tweetId','tweetUrl', 'search_query', 'text']

class Tweet():
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, search_query):
        self._tweets = None
        self._author = None
        self._mediaUrl = None
        self._tweetId = None
        self._tweetUrl = None
        self._auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self._auth.set_access_token(access_token, access_token_secret)
        self._api = tweepy.API(self._auth)
        self._search_query = search_query
    def __getattr__(self, attr):
      if attr in EXPECTED_ATTRIBUTES:
        value = getattr(self, '_' + attr)
        if value is None:
          raise ValueError(f'Value {attr} is None')
        return value
      #return getattr(self, attr)
    def randomTweet(self, type=None):
        isTypeImage = (type == "image")
        while True:
            if util.fileStuff.isMasterIdEmpty():
                util.writeids.getTwitterIds(self._auth, self._search_query, EndDate=today())
                continue
            elif util.used.isAllUsed():
                util.writeids.getTwitterIds(self._auth, self._search_query, EndDate=util.writeids.getLastMasterIdDate())
                continue

            self._tweets = util.fileStuff.readMasterId()
            self._tweetId = random.choice(list(self._tweets.values()))

            if (util.used.isIdUsed(self._tweetId)):
                continue
            else:
                try:
                    randomTweetInfo = self._api.get_status(id = self._tweetId, tweet_mode = "extended")
                    self._author = util.parseTweet.getTweetAuthor(randomTweetInfo)
                    if isTypeImage:
                        self._mediaUrl = util.parseTweet.getTweetMedia(randomTweetInfo)
                    self._tweetUrl = f"https://twitter.com/i/web/status/{self._tweetId}"
                    self._text = util.parseTweet.getTweetText(randomTweetInfo)
                    if ((not self._author) or (not self._mediaUrl and isTypeImage)): #if they return an empty string
                        util.used.appendId(self._tweetId)
                        continue
                except tweepy.error.TweepError:
                    util.used.appendId(self._tweetId)
                    continue
                util.used.appendId(self._tweetId)
                break
