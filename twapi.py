import twitter
import helpers
import time
import sys

class twitterapi:
  
  
  def __init__(self, consumer_key, consumer_secret, access_key, access_secret,encoding):
    '''Instantiates the twitter connection as well as the storage variables'''
    self.twapi = twitter.Api(consumer_key, consumer_secret, access_key, access_secret, encoding)
    self.last_reply_id = 0
    self.last_status = ''
    self.status_update_delay = 0
    self.last_deleted_message = ''



  def replies(self):
    '''Prints a string containing the number of replies.
    
    Does not return a value'''
    reply = self.twapi.GetReplies(None,self.last_reply_id)
    self.printl(str(len(reply))+" New Replies: Type 'read' to read the replies!!101!")



  def printl(self,string):
    '''Prints the supplied string with a carriage return character appended.
    
    Does not return a value'''
    print (string+"\r");



  def post(self,message):
    '''Posts the supplied message to the currently authenticated twitter account.
    
    Does not return a value'''
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




  def delete(self):
    '''Deletes last posted message and stores the text of that message for later undeletion.
    
    Does not return a value.'''
    if self.last_status != '':
      self.last_deleted_message = self.last_status.text
      self.twapi.DestroyStatus(self.last_status.id)
      self.printl("Last Post Deleted")
    else:
      self.printl("Error deleting status")




  def undelete(self):
    '''Posts the contents of last_deleted_message, if any.
    
    Does not return a value.'''
    if self.last_deleted_message != '':
      self.post(self.last_deleted_message)
      self.last_deleted_message = ''





  def read_replies(self):
    '''Pulls and displays any @replies made to the currently authenticated twitter account.
    
    Does not return a value.'''
    reply_list = self.twapi.GetReplies(None, self.last_reply_id)
    reply_list.reverse()
    
    for reply in reply_list:
      
      self.printl("    "+reply.user.screen_name+" said: "+reply.text)
      
      if reply.in_reply_to_status_id != None:
        self.printl("In reply to" + reply.in_reply_to_screen_name + ":" + self.twapi.GetStatus(reply.in_reply_to_status_id).text + "\n")
      else:
        self.printl("In reply to...no one?\n")
      
      self.last_reply_id = reply.id
      time.sleep(2)
  
