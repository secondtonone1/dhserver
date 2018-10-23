#-*-coding:utf-8-*-
import os
import sys

# Redis配置
redis_options = {
    'redis_host':'127.0.0.1',
    'redis_port':6379,
    'redis_pass':'',
}
 
# Tornado app配置
settings = {
    #'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    #'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
    #'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    #'xsrf_cookies':False,
    #'login_url':'/login',
    'debug':True,
}
 
# 日志
log_path = os.path.join(os.path.dirname(__file__), 'log')
proj_path = os.path.dirname(__file__)
dhport = 8898

