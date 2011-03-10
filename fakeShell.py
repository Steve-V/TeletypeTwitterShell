#!/usr/bin/env python


import time
import twitter
import sys
import twapi
import getopt
from helpers import *

#default: python50 my test account
consumer_key = '2x0h71VcEAk2dAdf886HmA';
consumer_secret = 'WWsaaEJOzCuRtUxhR2kU6LShZNyNBSufuKod91N1U';
access_key = '254290857-CrESL7rXpjMlJnaCqlTwANYS2J4dRObMbdqLTcM';
access_secret = 'voHU42UTprwkfEofwXFWtxnfUumwlxKMdAUB8fouIA';
encoding='utf-8';

if not consumer_key or not consumer_secret or not access_key or not access_secret:
  printl("error: consumer_key ,consumer_secret ,access_key ,access_secret need to be set");
  sys.exit(2);

api = twitter.Api(consumer_key, consumer_secret, access_key, access_secret, encoding);

message='';
last_deleted_message='';
last_status = None; #twitter.Status();
current_timezone=(time.timezone/60)/60; # Timezone
status_update_delay=0;# 0 or api.MaximumHitFrequency() <- 8
last_reply_id=0;

version_number = "0.14";

#------------------------------------------------------------
#printl appends carriage returns ...
def printl(string):
  print (string+"\r");

#------------------------------------------------------------
#time date functions, returns string
def current_time_date():
  timen=time.gmtime();
  return str(timen[3]-current_timezone)+":"+str(timen[4])+" "+str(timen[1])+"-"+str(timen[2])+"-"+str(timen[0]);

def current_time():
  timen=time.gmtime();
  return str(timen[3]-current_timezone)+":"+str(timen[4]);


def replies(): #displays # of replies
  global last_reply_id;
  reply=api.GetReplies(None,last_reply_id);
  printl(str(len(reply))+" New Replies: Type 'read' to read the replies");



def main():
  #replies()
  twa = twapi.twitterapi(consumer_key, consumer_secret, access_key, access_secret, encoding)
  twa.getResults()
  

if __name__ == '__main__':
  main()