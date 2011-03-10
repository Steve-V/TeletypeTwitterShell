import twitter

class twitterapi:
  
  def __init__(self, consumer_key, consumer_secret, access_key, access_secret,encoding):
    self.twapi = twitter.Api(consumer_key, consumer_secret, access_key, access_secret, encoding);
  
    