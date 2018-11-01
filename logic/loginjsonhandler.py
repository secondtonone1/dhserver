#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.web
import json
#http://localhost:8000/?greeting='wuchen'

class LoginJsonHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data=json.loads(self.request.body.decode('utf-8'))
            print("call LoginHandler success!!!")
            if('name' not in data):
                name='noname'
            else:
                name = data['name']
            if('password' not in data):
                password = 'nopassword'
            else:
                password = data['password']
            self.write(name + ' login success!'+' pass word is: '+ password)
            print(name + ' login success!'+' pass word is: '+ password)
        except :
            print('get_argument exception...')
    get = post
