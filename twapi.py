import twitter
import helpers
import time
import sys

class twitterapi:
  
  
  def __init__(self, consumer_key, consumer_secret, access_key, access_secret,encoding):
    self.twapi = twitter.Api(consumer_key, consumer_secret, access_key, access_secret, encoding)
    self.last_reply_id = 0
    self.last_status = ''
    self.status_update_delay = 0



  def replies(self): #displays # of replies
    reply = self.twapi.GetReplies(None,self.last_reply_id)
    self.printl(str(len(reply))+" New Replies: Type 'read' to read the replies!!101!")



  def printl(self,string):
    print (string+"\r");



  def post(self,message):
    
    self.printl("Processing ...\n")
    time.sleep(self.status_update_delay/4)
    
    try:
      last = self.twapi.PostUpdate(message)
      self.last_status = last
    except UnicodeDecodeError:
      self.printl("Your message could not be encoded.  Perhaps it contains non-ASCII characters?")
      self.printl("Try explicitly specifying the encoding with the --encoding flag")
      sys.exit(2)
        
    self.printl(last.user.name+" just posted: "+last.text);

    time.sleep(self.status_update_delay/8);
    self.printl("\r\nRemember: you can always use the delete command to remove your post and try again")

