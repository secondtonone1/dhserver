#-*-coding:utf-8-*-
import os
import sys
from indexhandler import IndexHandler
from loginhandler import LoginHandler
from loginjsonhandler import LoginJsonHandler
from fileuploadhandler import FileUploadHandler

callhandlers=[(r"/", IndexHandler),
              (r"/login", LoginHandler),
              (r"/login_json",LoginJsonHandler),
              (r"/upload_file",FileUploadHandler),
            ]