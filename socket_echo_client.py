# socket_echo_client.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

        # Send data
        message = b'This is the message.  It will be repeated.'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while True:
            data = sock.recv(2)
            # amount_received += len(data)#                                    
            print('received: ' + str(int.from_bytes(data,"big")))
            sock.sendall(b'Next data.')  
finally:
        print('closing socket')
        sock.close()
