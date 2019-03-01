try:
	import subprocess
	subprocess.Popen(["server.exe"])
except:
	print("Server.exe not found? Move all files to same directory and relaunch or launch server.exe manually.")
import sys
httpd=None
try:
	if sys.version_info[0] is 3:
		import http.server
		print("Launching HTTP server! (Python 3.x)")
		class ServerHandler(http.server.BaseHTTPRequestHandler):
			def do_POST(self):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("server|35.231.10.97\nport|17091\ntype|1\n#maint|Mainetrance message (Not used for now) -- Growtopia Noobs\n\nbeta_server|35.196.222.216\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
			def do_GET(self):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("server|35.231.10.97\nport|17091\ntype|1\n#maint|Mainetrance message (Not used for now) -- Growtopia Noobs\n\nbeta_server|35.196.222.216\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
			def log_message(self, format, *args):
				return
		server_address = ('', 80)
		httpd = http.server.HTTPServer(server_address, ServerHandler)
		print("HTTP server is running! Don't close this or GT will be unable to connect!")
		httpd.serve_forever()
	else:
		import SimpleHTTPServer
		import SocketServer
		print("Launching HTTP server! (Python 2.x)")
		class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
			def do_POST(self):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("server|35.231.10.97\nport|17091\ntype|1\n#maint|Mainetrance message (Not used for now) -- Growtopia Noobs\n\nbeta_server|35.196.222.216\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
			def do_GET(self):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("server|35.231.10.97\nport|17091\ntype|1\n#maint|Mainetrance message (Not used for now) -- Growtopia Noobs\n\nbeta_server|35.196.222.216\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
			def log_message(self, format, *args):
				return
		#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
		Handler = ServerHandler
		httpd = SocketServer.TCPServer(("", 80), Handler)
		print("HTTP server is running! Don't close this or GT will be unable to connect!")
		httpd.serve_forever()
except:
	print("Port 80 is probably already used? Try close anything what can be running there or try run this app as Admin.")
