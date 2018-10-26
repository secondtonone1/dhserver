#-*-coding:utf-8-*-
import pymongo
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MongoDbSingle(Singleton):
    def initDb(self,addr='',port=0,dbname=''):
        try:
            self.client = pymongo.MongoClient(addr, port)
            self.db=self.client[dbname]
            return True
        except:
            print('initDb error!!')
            return False       
    #setname is collection str, data is dict of json whic to save
    #data = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
    def insertData(self,setname='',*,data={}):
        try:
            mycol = self.db[setname]
            mydoc = mycol.find(data)
            #if (mydoc.count()!=0):
               # return True
            mycol.insert_one(data)
            return True;
        except:
            print("insert failed")
            return False
    #setname is collection str, query={"name":"wuchen"}
    def getData(self,setname='',*,query={}):
        try:
            mycol = self.db[setname]
            mydoc = mycol.find(query).limit(1)
            if(mydoc is None):
                return None
            return mydoc[0]
        except:
            print("get data failed")
            return None

    #myquery = { "name": { "$regex": "^F" } }
    #newvalues = { "$set": { "alexa": "123" } }
    def updateData(self, setname='',*,query={}, newvalues={}):
        try:
            mycol = self.db[setname]
            newdata={"$set":newvalues}
            mycol.update_one(query, newdata)
        except:
            print("update Data failed")
    
    def delData(self,setname='',*,query={}):
        try:
            mycol = self.db[setname]
            mycol.delete_many(query)
        except:
            print("del data failed")
       

_mongoInstance = MongoDbSingle()
_mongoInstance.initDb('127.0.0.1',29017,'dhhome')
datas = { "name": "test3333444", "password": "123456" }
_mongoInstance.insertData('userbase',data=datas)
print(_mongoInstance.getData('userbase',query={"name":"test"}))
_mongoInstance.updateData('userbase',query={"name":"test"},newvalues={"name":"teacher cai"})
print(_mongoInstance.getData('userbase',query={"name":"teacher cai"}))




 
