#-*-coding:utf-8-*-
import sys
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from config import dhport
from config import settings
from config import proj_path
logic_path = os.path.join(proj_path, 'logic')
sys.path.append(logic_path)
from factorycall import callhandlers


#http://localhost:8000/?greeting='wuchen'
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=callhandlers,**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(dhport)
    tornado.ioloop.IOLoop.instance().start()