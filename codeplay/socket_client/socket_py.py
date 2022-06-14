import socket

serv_sock = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM,
                          proto=0)

serv_sock.bind(('', 53210))
backlog = 10
serv_sock.listen(backlog)

while True:
    client_sock, client_addr = serv_sock.accept()

    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        client_sock.sendall(data)

    client_sock.close()