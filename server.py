#!/usr/bin/python           # This is server.py file

import socket         

s = socket.socket()         
host = socket.gethostname() 
port = 12345       
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))        
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)                 
while True:
	c, addr = s.accept()     
        name=raw_input("Enter your name: ")
	c.send(name)
	name1 = c.recv(102400)
	print "Connnection Established with",name1
	print 'Enter "EXIT" to close the connection'
        while(1):
		message=raw_input(name+": ")
        	c.send(message)
		if(message=="EXIT"):
			print "Connection Closing"
			break
		message1= c.recv(102400)
		print name1+": "+message1
		if(message1=="EXIT"):
			print "Connection Closing"
			break
        c.close()
	if(message=="EXIT"):
		break
	if(message1=="EXIT"):
		break
s.close
