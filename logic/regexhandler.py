#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
#from config import settings

#http://localhost:8000/?greeting='wuchen'
class RegexHandler(tornado.web.RequestHandler):
    '''
    def get(self,param1,param2):
        try:
            print('regex data1 is %s' %(param1) )
            self.write('regex data1 is %s;' %(param1))
            print('regex data2 is %s' %(param2) )
            self.write('regex data2 is %s;' %(param2))
            str1='http://127.0.0.1:8898/test/'
            str2='/regex'
            self.write('we recive path is %s;' %(str1+param1+'/'+param2+str2))
        except:
            print('get regex argument exception')
    '''
    def get(self,*param):
        try:
            print('regex data1 is %s' %(param[0]) )
            self.write('regex data1 is %s;' %(param[0]))
            print('regex data2 is %s' %(param[1]) )
            self.write('regex data2 is %s;' %(param[1]))
            str1='http://127.0.0.1:8898/test/'
            str2='/regex'
            self.write('we recive path is %s;' %(str1+param[0]+'/'+param[1]+str2))
        except:
            print('get regex argument exception')
    post = get   