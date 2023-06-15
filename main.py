from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

request_cnt = 0
class test:
    def show(self):
        content = f"zhijxu, the client addr is {self.client_address}\n"
        return bytes(content, 'utf-8')

class http_server:
    def __init__(self, port):
        print(f"this is a simple http server, will listen at port {port}")
        server = HTTPServer(('', port), myHandler)
        server.serve_forever()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global request_cnt
        request_cnt += 1
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        print(f"get {request_cnt}th request from {self.client_address}") # log in server stdout
        content = f"zhijxu, server hostname is {socket.gethostname()}, the client addr is {self.client_address}\n"
        self.wfile.write(bytes(content, 'utf-8'))
        return

class main:
    def __init__(self, port):
        self.server = http_server(port)

if __name__ == '__main__':
    import sys
    print("main function is going to start http server")
    m = main(int(sys.argv[-1]))