import socket

s = socket.socket()

host = socket.gethostname()
print(host)
port = 1235
s.bind((host, port))

s.listen(10)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()