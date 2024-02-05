# Introduction to Dynamic Web Content

## Web Applications and the Request/Response Cycle

- Browser makes a request to web server
- Click on a tag you get a new web page

## Exploring the HyperText Transfer Protocol

- The protocol broswers use to talk to servers
- Uniform Resource Locator http:// (protocol) data.pr4e.org (host) /page1.htm ( document)
- Invented to retrieve images and documents
- Made in 1990
- Connect to a server figure out where it is, send out a command and get something in return
- the sockets are the things that make the phone call
- Http is what we do once the phone call is established
- IETF made internet standrads
- Connect to a server through the socket and request a document

## Using Sockets to Make Network Connections in Python

- Network sockets are like phone calls for computers
- There isnt a perminant connection to the data
- Application process <-internet-> Application process
- A protocol for who talks first
- A port is an application-spefic or process-specfic software communications endpoint

## Building a Simple Web Browser in Python
``` 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org?page1.tm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data=mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode(),end='')
mysock.close()
``` 
