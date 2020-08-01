#! /usr/bin/python

import socket
import thread

def reply(conn):
	while True:
		data = conn.recv(1024)
		conn.send("Server"+data)

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('127.0.0.1',8000))
	sock.listen(5)
	conn,addr = sock.accept()
	print "got connection from",addr
	start_new_thread(reply, (conn,))

finally:
	print "Closing socket"
	sock.close()

	
