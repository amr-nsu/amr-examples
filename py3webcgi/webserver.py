from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ('', 8000)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print('Started at {0}:{1}'.format(*server_address))
httpd.serve_forever()
