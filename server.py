import entertainment_center
import fresh_tomatoes

fresh_tomatoes.open_movies_page(entertainment_center.movies)


# import SimpleHTTPServer
# import SocketServer

# class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = '/fresh_tomatoes.html'
#         return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

# PORT = 8080
# Handler = MyRequestHandler
# server = SocketServer.TCPServer(('0.0.0.0', PORT), Handler)

# server.serve_forever()