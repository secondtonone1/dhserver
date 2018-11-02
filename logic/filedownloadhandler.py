#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.web
import json
import os
import sys
#http://localhost:8000/?greeting='wuchen'

class DownUploadHandler(tornado.web.RequestHandler):
    def post(self):
        filename = self.get_argument('filename','Empty')
        if(filename=='Empty'):
            return
        print('i download file handler : ',filename)
        upload_path = os.path.join(os.path.dirname(__file__), 'files')
        file_path = os.path.join(upload_path, filename)
        if(os.path.exists(file_path)==False):
            return
        #Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
        self.set_header ('Content-Type', 'application/octet-stream')
        self.set_header ('Content-Disposition', 'attachment; filename='+filename)
        #读取的模式需要根据实际情况进行修改
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024*1024)
                if not data:
                    break
                self.write(data)
        #记得有finish哦
        self.finish()
        print('send success !!!')
    get = post


