#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.web
import json
import os
import sys
#http://localhost:8000/?greeting='wuchen'

class FileUploadHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            upload_path = os.path.join(os.path.dirname(__file__), 'files')  # 文件的暂存路径
            if(os.path.exists(upload_path)==False):
                os.makedirs(upload_path)
            file_metas = self.request.files.get('files', None)  # 提取表单中‘name’为‘file’的文件元数据

            if not file_metas:
                return 

            for meta in file_metas:
                filename = meta['filename']
                file_path = os.path.join(upload_path, filename)
                if(os.path.exists(file_path)):
                    continue

                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
                # OR do other thing
        except IOError as e:
            print(e.errno)
            print(e.strerror)
        except :
            print('get_argument exception...')
    get = post


