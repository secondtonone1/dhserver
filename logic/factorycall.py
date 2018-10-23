#-*-coding:utf-8-*-
import os
import sys
from indexhandler import IndexHandler
from loginhandler import LoginHandler

callhandlers=[(r"/", IndexHandler),
              (r"/login", LoginHandler),
            ]