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
from singletonclass import MongoDbSingle
from singletonclass import _mongoInstance
if __name__ == "__main__":
    #_mongoInstance3 = MongoDbSingle()
    #print(_mongoInstance is _mongoInstance3)
    app = tornado.web.Application(handlers=callhandlers,**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(dhport)# listen local only "127.0.0.1"
    tornado.ioloop.IOLoop.instance().start()