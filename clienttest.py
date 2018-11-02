#-*-coding:utf-8-*-
import requests
import json
urlcode = 'http://127.0.0.1:8898'
payload = {'name': 'wuchen', 'password': '123456'}
import os, sys
def requestwrapper(requestfunc):
    def wrapperrequest(*args,**kwargs):
        ret=requestfunc(*args,**kwargs)
        if ret:
            print(ret.url)
            #print(ret.text)
        return ret
    return wrapperrequest

posturls='http://127.0.0.1:8898/login'
@requestwrapper
def getrequest(urls=''):
    ret=requests.get(urls,timeout=5)
    return ret
@requestwrapper
def postrequest(urls='', datas={}):
    ret=requests.post(urls,data=datas,timeout=5)
    return ret

@requestwrapper
def postjsonrequest(urls='',datas={}):
    header = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
    response = requests.post(urls, headers=header, data=json.dumps(datas),timeout=5)    ## post的时候，将data字典形式的参数用json包转换成json格式。
    return response

@requestwrapper
def postfilerequest(urls='',datas={},filepath=''):
    file = {"files" : open(filepath, "rb") }
    response = requests.post(urls, files=file , data=datas,timeout=5)    ## post的时候，将data字典形式的参数用json包转换成json格式。
    return response

@requestwrapper
def downfilerequest(urls='',datas={},filename=''):
    datas['filename'] = filename
    r = requests.post(urls,data=datas,timeout=15)
    download_path = os.path.join(os.path.dirname(__file__), 'download')
    if(os.path.exists(download_path)==False):
        os.makedirs(download_path)
    filename = os.path.join(download_path,filename)
    if(os.path.exists(filename)):
        return None
    with open(filename,'wb') as f:
        f.write(r.content)
    return r
    

    
if __name__ == "__main__":
    try:
        getrequest(urlcode)
        postrequest(posturls,payload)
        postjsonrequest('http://127.0.0.1:8898/login_json',payload)
        postfilerequest('http://127.0.0.1:8898/upload_file',payload,'test.jpg')
        downfilerequest('http://127.0.0.1:8898/download',payload,'test.jpg')
    except requests.exceptions.ReadTimeout:
        print('request time out...')