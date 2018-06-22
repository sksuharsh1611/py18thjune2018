#!/usr/bin/python2

import time,webbrowser,commands

menu='''

press 1: To check current date and time:
press 2: To scan all your Mac Address in your current cOnnected Network:
press 3: To shutdown your machine after 15 minutes:
press 4: To search something on Google:
press 5: To logout your current machine:
press 6: To shutdown all cOnnected system in your current Network:
press 7: To Update status on your Facebook:
press 8: To list Ip Addresses of given Website:

'''
print  menu

choice=raw_input("Enter your choice:")

if  choice  ==  '1' :
	print  "current date and time is :   ",time.ctime()

elif choice == '2' : 
	x=commands.getoutput('cat /sys/class/net/*/address')
	print x

elif choice == '3' :
	print "Your system is being shutting down after 15 minutes"
	commands.getoutput("sudo shutdown +1")
	

elif  choice  ==  '4' :
	find=raw_input("enter your query : ")
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)

elif choice == '5' :
	print "logging out from your current machine: "
	commands.getoutput("exit")

#elif choice == '6' :

elif choice == '7':
	print "update status in facebook"
	username=raw_input("enter your username : ")
	passwd=raw_input("enter your password : ")	
	webbrowser.open_new_tab("https://touch.facebook.com/login/")

elif choice == '8' :
	web=raw_input("enter your website : ")
	ip=commands.getoutput("host "+web)
	print ip

else :
	print  "Invalid OPtion"



