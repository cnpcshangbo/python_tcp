# socket_echo_server.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        # Sending continous msg
        msg_no = 0;
        while msg_no < 3000:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            # if data:
            #    print('sending data back to the client')
            #    connection.sendall(data)
            # else:
            #    print('no data from', client_address)
            #    break
            # connection.sendall(msg_no.to_bytes(2, 'big'))
            # connection.sendall(str.encode(str(msg_no)))
            print(str(msg_no).encode())
            connection.sendall(str(msg_no).encode())
            msg_no+=1

    finally:
        # Clean up the connection
        connection.close()
