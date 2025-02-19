import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive some data
res = client.recv(4096)

print(res.decode())
