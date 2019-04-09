import pymongo

#创建连接
client = pymongo.MongoClient('test.ipay.so',58019)
#连接数据库
db = client['config']
db.authenticate("config","config")
#连接表
collection = db['agent']

# print(collection.find_one())
# 构建数据
for i in range(2000):
    data = {
    "_id" : "asd1"+str(i),
    "agentCode" : "10130001",
    "agentName" : "IrisTest POSP",
    "fullName" : "IrisTest POSP",
    "agentType" : "NumberInt(5)",
    "accountManager" : "测试",
    "city" : "上海市",
    "isGenerateFlow" : "NumberInt(1)",
    "flowFileType" : "NumberInt(255)",
    "instituteLevel" : "NumberInt(1)",
    "agentClass" : "NumberInt(0)",
    "settleMode" : "NumberInt(2)",
    "wxpCost" : 0.6,
    "alpCost" : 0.7,
    "bdpCost" : 0.8,
    "contactAddress" : "中科路699号",
    "bizContactPerson" : "12",
    "bizContactTelephone" : "13758745612",
    "bizContactEmail" : "111@qq.com",
    "oprContactPerson" : "3456",
    "oprContactTelephone" : "021-60278098",
    "oprContactEmail" : "222@qq.com",
    "bankName" : "浦发银行大庆分行营业部",
    "bankNO" : "310265000011",
    "bankAccount" : "6321458971133652",
    "profitSharingAccount" : "机构浦发本行",
    "createTime" : "2016-01-15 10:14:46",
    "updateTime" : "2019-02-20 18:22:18",
    "status" : "1",
    "schemeCode" : "000024",
    "schemeName" : "网商银行渠道才汇方案",
    "settMode" : "T1",
    "positiveTransAmtPercent" : 100.0,
    "isNeedRisk" : "true"
    }
    collection.insert(data)




