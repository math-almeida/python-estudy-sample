import socket

host = "0.0.0.0"
port = 9998

# socket object
'''
socket.AF_INET indicate socket will be Ipv4
socket.SOCK_STREAM indicates that will be a TCP client
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to client
'''
Since is a TCP client, we must connect to send data
'''
client.connect((host, port))

# send data
client.send(b"GET/HTTP/1:1\n\r\nHost:google.com\r\n\r\n")

# receive data
response = client.recv(4096)
print(response.decode())

# close connection
client.close()

'''
This code was provided by Black Hat Python book
Serve as example and study about networks
It made some assumptions about sockets

1 - The connection will always be succed

2 - The server expects us to send data first
(some servers expect to sendo data to you first and await response)

3 - This server always return data in a timely fashion

They make this assumptions for simplicity
'''
