#-*-coding:utf-8-*-
import requests

urlcode = 'http://192.168.1.172:8898'
payload = {'name': 'wuchen', 'password': '123456'}

def requestwrapper(requestfunc):
    def wrapperrequest(*args,**kwargs):
        ret=requestfunc(*args,**kwargs)
        print(ret.url)
        print(ret.text)
        return ret
    return wrapperrequest

posturls='http://192.168.1.172:8898/login'
@requestwrapper
def getrequest(urls=''):
    ret=requests.get(urls,timeout=5)
    return ret
@requestwrapper
def postrequest(urls='', datas={}):
    ret=requests.post(urls,data=datas,timeout=5)
    return ret

if __name__ == "__main__":
    try:
        getrequest(urlcode)
        postrequest(posturls,payload)
    except requests.exceptions.ReadTimeout:
        print('request time out...')