#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.web
#http://localhost:8000/?greeting='wuchen'
class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')