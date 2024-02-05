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
- create socket in your computer
- socket.scoet makes the phone
- mysock.connect dials the phone
- Browser developer mode is how you debug the code

## Building a Simple HTTP Server in Python

- The server already exists it sits and waits for it to be talked to
- listen(5) means that the OS will hold up to 4 other requests if it currently is working on one
- The recive and the send is the same function
- The server recives it as utf-8 and needs to decode it into unicode
- To send data it has to be utf-8
- As soon as the server sends the data it shutdowns the socket.(hangs up the phone)
- The server is an infinate loop
- The server is destined to wait until a client connects to it

## Understanding Browser Developer Mode

- It grabs all the links, CSS, fonts and javascript and builds up the amount of request and the time it takes to get them

## the HTTP request/response cycle

When the server receives that request, it uses the information included in the request to build a response that contains the requested information.

## what a socket is
- a way of connecting two nodes on a network to communicate with each other.

## most common tcp port numbers 
- http - 80

