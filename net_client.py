import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ("localhost", 10390)
    sock.connect(addr)
    print(sock)
    
    for i in range(1, 101):
        msg = str(i)
        sock.sendall(msg.encode())
        reply = sock.recv(1024).decode()
        print(reply)
    
    sock.close()
main()