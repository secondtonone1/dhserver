#-*-coding:utf-8-*-
import os
import sys
from indexhandler import IndexHandler
from loginhandler import LoginHandler
from loginjsonhandler import LoginJsonHandler
from fileuploadhandler import FileUploadHandler
from filedownloadhandler import DownUploadHandler
from regexhandler import RegexHandler

callhandlers=[(r"/", IndexHandler),
              (r"/login", LoginHandler),
              (r"/login_json",LoginJsonHandler),
              (r"/upload_file",FileUploadHandler),
              (r"/download",DownUploadHandler),
              (r"/test/(.*?)/(.*?)/regex",RegexHandler),
            ]