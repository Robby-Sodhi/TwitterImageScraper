import tweepy
import datetime
from fileStuff import writeMasterIds, readMasterId


def parseDate(date):
    date = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
    return date.strftime("%Y%m%d%H%M")

def today():
    return ((datetime.date.today()).strftime("%Y%m%d%H%M"))

def getLastMasterIdDate():
    data = readMasterId()
    lastDate = list(data.keys())[-1]
    return lastDate

def getTwitterIds(auth, search, EndDate, StartDate=201101012315):
    api = tweepy.API(auth)
    """
    tweepySearch = tweepy.Cursor(api.search_full_archive,
    environment_name = "development",
    query = search,
    maxResults = 100,
    fromDate = StartDate,
    toDate=EndDate
    ).items(1000)
    """
    tweepySearch = tweepy.Cursor(api.search, q=search, count=100).items(1000)
    ran = False
    TweetData = {}
    for tweet in tweepySearch:
        ran = True
        try:
            tweet.retweeted_status
            continue
        except AttributeError: #not a retweet
            pass
        formattedDate = parseDate(tweet.created_at)
        TweetData.update({formattedDate: tweet.id})
    if not ran:
        raise LookupError("No tweets found")
    writeMasterIds(TweetData)
