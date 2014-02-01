#!/usr/bin/python           # This is client.py file

import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                

s.connect((host, port))
name1= raw_input("Enter your name: ")
s.send(name1)
name=s.recv(102400)
print "Connection Established with",name
print 'Enter "EXIT" to close the connection'
while(1):
	message = s.recv(102400)
	print name+": "+message
	if(message=="EXIT"):
		print "Connection Closing"
		break
	message1=raw_input(name1+": ")
	s.send(message1)
	if(message1=="EXIT"):
		print "Connection Closing"
		break
s.close                   
