from socketserver import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting')
        #self.wfile.write(b'abc')

server = TCPServer(('', 1235), Handler)
server.serve_forever()