import pymongo
import base64

#创建连接
client = pymongo.MongoClient('localhost',port=8080)
#连接数据库
db = client['db']
db.authenticate("db","db")
#连接表
collection = db['table']

# print(collection.find_one())
# 构建数据
for i in range(10):
    data = {
    "_id" : "asd20"+str(i),
    "name":"cyt"
    }
    collection.insert(data)


#加解密
a = 'test123'
encode_str = base64.encodebytes(a.encode('utf8'))
print(encode_str)
c = base64.b64decode(encode_str).decode("utf-8")
print(c)





