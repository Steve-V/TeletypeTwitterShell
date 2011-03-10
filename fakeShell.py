#!/usr/bin/env python


import time
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

version_number = "0.14";

status_update_delay = 0

#------------------------------------------------------------

# command: Gets input from the command line
def command():
  cmd=str(raw_input(current_time()+" Command >")).lower();  # make the command all lowercase for usage
  time.sleep(status_update_delay/8);
  printl("");

  # command input was empty 
  if not cmd:
    return True; # ignore

  #display about help
  if cmd=="about" or cmd=="a":
    about();
    return True;

  #get command help
  if cmd=="?" or cmd=="help" or cmd=="h":
    help(); # prints help text
    return True;

  #post tweet
  if cmd=="post" or cmd=="p":
    printl("Type message, maximum 140 characters, newline to finish");
    printl("Feel free to include you name so others know who's posting");
    inputs=str(raw_input("> "));
    if len(inputs) <= 10: #python_twitter wont accept it if its less than 10
      printl("Message must be more than 10 characters");
      
      post_loop = True
      while(post_loop):
        i=str(raw_input("post anyways ? [Yes/No] ")).lower();
        if i=="yes":
          post(inputs+"...........");
          post_loop = False
        if i=="no":
          post_loop = False
        printl("Yes or No");
      return True

    if len(inputs) > 140:
      printl("Message must be less than 140 characters");
      return True;

    post(inputs);
    return True;

  #deletes the last post
  if cmd=="delete" or cmd=="d":
    while(1):
      i=str(raw_input("Delete you last post ? [Yes/No]")).lower();
      if i=="yes":
        if last_status!=None:
          delete(last_status);
        else:
          printl("You must post before you can delete your post !");
        break;
      if i=="no":
        break;
      printl("Please type Yes or No");
    return True


  #undelete's the last post if it was deleted
  if cmd=="undelete" or cmd=="u":
    undelete();
    return True;
    
  #read command
  if cmd=="read" or cmd=="view" or cmd=="r":
    read_replies();
    return True;


  #exit command
  if cmd=="exit" or cmd=="quit" or cmd=="q":
    q=str(raw_input("Really [Yes/No]\a")).lower();

    if q=="y" or q=="yes":
      printl("Goodbye");
      return False;
    else:
      printl("Thank You");
      return True;
  
  bad_command(); #it wasn't a recognized command
  return True;




def main():
  
  twa = twapi.twitterapi(consumer_key, consumer_secret, access_key, access_secret, encoding)
  
  print "check"
  
  #twa.replies()
  #twa.post("frobz4")
  #twa.delete()
  #twa.undelete()
  #twa.read_replies()
  
  command()
  
if __name__ == '__main__':
  main()