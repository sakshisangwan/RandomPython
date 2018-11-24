#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print('waiting for connection...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('...connected from: ', addr)
	print('...port: ', getservbyname('daytime'))

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send(b'[%s] %s' % (ctime().encode('utf-8'), data))
	tcpCliSock.close()
tcpSerSock.close()	