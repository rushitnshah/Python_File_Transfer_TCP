import socket

s = socket.socket()
host = input(str("Please enter the host address of the sender : "))
port = 8080
s.connect((host,port))
print("Connected...")

filename = input(str("Specify save path for incoming file: "))
file = open(filename, 'wb')
buffsize = 4096
file_data = s.recv(buffsize)
file.write(file_data)
file.close()
print("File has been received successfully.")
