#!/usr/bin/python

import commands
import socket
#            type of ipV4 , type of protocol UDP
socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind current and port
#           ip    ,      port
s.bind(("192.168.10.235",8000))

#buffer size that means data recv by per client at single send
for i in range(10000) :
	data=s.recvfrom(100) 
	print data
	print commands.getoutput(data[0])
'''
for i in range(10000):
	data=s.recvfrom(100)
	if 'date' in data[0] :
		print data[0]
		print commands.getoutput('date')
	elif 	'cal' in data[0]:
		print commands.getoutput('cal')
	else :
		print data
'''


