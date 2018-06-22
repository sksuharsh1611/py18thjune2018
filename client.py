#!/usr/bin/python

import  socket 
#            type of ipv4 ,    type of protocol UDP  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(10000) :
	cmd=raw_input("Enter any Linux Command: ")
	s.sendto(cmd,("192.168.10.182",8000)

#s.sendto("hello python",("192.168.10.182",8000))




