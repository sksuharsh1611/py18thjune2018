#!/usr/bin/python

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
	print "please wait internet cable is being checked.."

elif x == '2' :
	print "Internet connectivity is checking in a while"

elif x == '3' :
	print "Loading Google web page //"

else :
	print  "wrong option" 
