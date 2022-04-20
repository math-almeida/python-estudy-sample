import socket
import threading

IP = '0.0.0.0'
PORT = 9998


def main():
    '''
    First we tell to server to listen with a maximum backlog of 5 connections
    Then we put the server in this main loop waiting for incoming connections
    '''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'|*| Listening in {IP}:{PORT}')

    '''
    When a client connects we receive client socket in client var and remote
    connection details in address var
    Then we create a new thread obj that points to hancle_client passing the
    client socket obj as argument
    In this point the main server loop is ready to handle annother incomming
    connection
    '''
    while True:
        client, address = server.accept()
        print(f'|*| Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target = handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    '''
    The handle_client function performs a recv() and send a simple message back
    to the client
    '''
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'|*| Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()
