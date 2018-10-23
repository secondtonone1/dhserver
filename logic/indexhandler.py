#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from config import settings

#http://localhost:8000/?greeting='wuchen'
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')