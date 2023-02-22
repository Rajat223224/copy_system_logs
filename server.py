import socket

import logging

# Set up logging
logging.basicConfig(filename='F:/python project/file transfer/server-file.txt', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')    
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


##Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')
print('capture a file...')

while True:
    # Establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Get data from the client
    data = con.recv(1024)
    print(data.decode())
    file = open('server-file.txt', 'rb')
    line = file.read(1024)
    # Keep sending data to the client
    while(line):
        con.send(line)
        line = file.read(1024)
    
    file.close()
    print('File has been transferred successfully.')

    con.close()
