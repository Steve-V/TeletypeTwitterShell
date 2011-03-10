import time

version_number = "0.14";
current_timezone=(time.timezone/60)/60; # Timezone

#time date functions, returns string
def current_time_date():
  timen=time.gmtime();
  return str(timen[3]-current_timezone)+":"+str(timen[4])+" "+str(timen[1])+"-"+str(timen[2])+"-"+str(timen[0]);

def current_time():
  timen=time.gmtime();
  return str(timen[3]-current_timezone)+":"+str(timen[4]);



#------------------------------------------------------------
#printl appends carriage returns ...
def printl(string):
  print (string+"\r");


#------------------------------------------------------------
#usage text
def usage():
  printl("");
  printl("Usage: twitshell.py [-p message_content] [-r]");
  printl("Options:");
  printl("  -h    Show this help and exit --help");
  printl("  -v    Version information --version");
  printl("  -p [message]  Post a tweet containing [message] --post");
  printl("  -r    Read(and Display) recent replies --read");

#------------------------------------------------------------
#about text
def about():
  printl("Twitter Shell Version "+version_number);
  printl("  By Jason White, February 20 2011");
  printl("");
  printl("Special Thanks to:");
  printl("  Alphageek");
  printl("  BatSteve");# why don't you ever add yourself ?
  printl("  maglinvinn");
  printl("  MrTransistor");
  printl("  Quick_Ben");
  printl("  Sparky Projects");
  printl("  Tmb");
  printl("  Tysk");
  printl("  and everyone else in the forums !");
  printl("");
  printl("This program takes the output of a Teletype machine");
  printl("and allows the user to post it to twitter. It is a ");
  printl("fairly simple python script using the python-twitter");
  printl("module to interface with twitter");
  printl("");
  printl("This Program is licensed under the Modified BSD license");
  printl("  Program Copyright (C) 2011 Jason White\n");
#------------------------------------------------------------
#banner text
def banner():
  printl("  Twitter Shell Version "+version_number);
  printl(" Because the geek shall inherit the earth");
  printl("");

#------------------------------------------------------------
#bad command text
def bad_command():
  printl("Unknown command type ? or help for help");

#------------------------------------------------------------
#Help Me ! Text
def help():
  printl("Help Me ! - Commands:");
  printl("");
  printl("  [a] or about  - more info about this program");
  printl("  [d] or delete - delete the last message");
  printl("  [h] or help - this help text");
  printl("  [r] or read - read replies");
  printl("  [u] or undelete - undelete the last post, if it was deleted");
  printl("  [p] or post - post a message to twitter");
  printl("  [q] or quit - quit this program");
  printl("");
  printl("  Twitter Shell "+version_number+" For The Geek Group");
  printl("   By Jason White February 20 2011\n");
