def getTweetAuthor(tweetObject):
    try:
        data = tweetObject.author.screen_name
        return data
    except AttributeError:
        return ""
def getTweetMedia(tweetObject):
    try:
        data = tweetObject.extended_entities["media"][0]["media_url"]
        return data
    except AttributeError:
        return ""
def getTweetText(tweetObject):
    try:
        data = tweetObject.full_text
    except AttributeError:
        try:
            data = tweetObject.text
        except AttributeError:
            raise ValueError("text/Full_text missing")
    return data
