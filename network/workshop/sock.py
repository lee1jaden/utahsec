import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 12345))
s.listen(5)
print("Server is listening on port 12345")

while True:
    s, addr = s.accept()
    print("Got connection from", addr)
    s.sendall("Our working socket")
    s.close()
