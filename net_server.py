import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ("localhost", 10390)
    sock.bind(addr)

    sock.listen(5)
    while True:
        (connectedSock, clientAddress) = sock.accept()
        print("Connected to Socket")
        while True:
            try:
                msg = connectedSock.recv(1024).decode()
                if (len(msg)) == 0:
                    connectedSock.close()
                    print("Connection has been closed")
                    break
                print("Here is the data: " + msg)
                connectedSock.sendall(msg.encode())
            except:
                connectedSock.close()
        

    
main()


    
