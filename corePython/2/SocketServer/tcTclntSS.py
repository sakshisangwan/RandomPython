#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = input('> ')
	if not data:
		break
	tcpCliSock.send(b'%s\r\n' % data.encode('utf-8'))
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print(data.strip())
	tcpCliSock.close()