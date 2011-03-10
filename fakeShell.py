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

message='';
last_deleted_message='';
last_status = None; #twitter.Status();
status_update_delay=0;# 0 or api.MaximumHitFrequency() <- 8

version_number = "0.14";

#------------------------------------------------------------



def main():
  
  twa = twapi.twitterapi(consumer_key, consumer_secret, access_key, access_secret, encoding)
  
  print "check"
  
  #twa.replies()
  #twa.post("frobz4")
  #twa.delete()
  #twa.undelete()
  twa.read_replies()
  
if __name__ == '__main__':
  main()