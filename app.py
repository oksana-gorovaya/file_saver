import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from InputSaver import InputSaver


class HttpProcessor(BaseHTTPRequestHandler):
   def _set_headers(self):
       self.send_response(200)
       self.send_header('Content-type', 'text/html')
       self.end_headers()

   def do_GET(self):
       self._set_headers()
       f = open('./templates/task.html')
       self.wfile.write(f.read())

   def do_POST(self):
       try:
           form = cgi.FieldStorage(
               fp=self.rfile,
               headers=self.headers,
               environ={
                   'REQUEST_METHOD': 'POST',
                   'CONTENT_TYPE': self.headers['Content-Type'],
               }
           )

           return InputSaver(form).save_data()

       except Exception as e:
           print e

serv = HTTPServer(("localhost",8090),HttpProcessor)
serv.serve_forever()

