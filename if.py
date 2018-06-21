#!/usr/bin/python

import commands,time,webbrowser
'''
#raw_input always accept data in string format
n=raw_input("please enter a number: ")
n1=raw_input("Enter another number: ")


#print type(n)
#typecasting from string to integer

print int(n) + int(n1)
'''

option='''
press 1 to check Internet cable on your machine:
press 2 to check Internet access:
press 3 to check for Google access
'''

print option

x=raw_input()

if x == '1' :
	print "please wait internet cable is being checked by current OS.."
	time.sleep(3)	
	cable_check=commands.getoutput('sudo mii-tool eno1')
	if 'link ok' in cable_check:
		print "Lan cable is cOnnected"
		
	else:
		print "Lan Cable is not cOnnected"
		
elif x == '2' :
	print "Internet connectivity is checking in a while"

elif x == '3' :
	print "Loading Google web page //"
	find=raw_input("enter your query : ")
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)

else :
	print  "wrong option" 
