import pymongo

#创建连接
client = pymongo.MongoClient('localhost',port)
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




