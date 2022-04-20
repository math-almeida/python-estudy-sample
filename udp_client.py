import socket

host = "127.0.0.1"
port = 9997

# create socket object
'''
socket.AF_INET indicates socket will use Ipv4
socket.SOCK_DIAGRAM indicates socket will be a UDP client
'''
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
'''
There's no need to call connect() in UPD client we simply pass sendto()
UDP is a connectionless protocol
'''
client.sendto(b"AAABBBCCC", (host, port))

# receive some data
'''
We need to cal recvfrom() to receive UDP data back
Notice it returns both data and details of the remote host and port
'''
data, addr = client.recvfrom(4096)
print(data.decode())

# close socket object
client.close()
