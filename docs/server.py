import http.server
import socket
import socketserver

# tasklist
# /IM py37.exe /F
#

PORT = 8000
print(f'serving on: {socket.gethostbyname(socket.gethostname())}')

with socketserver.TCPServer(('', PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print('PORT:', PORT)
    httpd.serve_forever()
