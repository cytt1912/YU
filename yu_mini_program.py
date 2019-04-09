import pymysql

db = pymysql.connect("192.168.1.177","test","cardinfolink","msp")
cursor = db.cursor()
for i in range(10000):
    cursor.execute(
        "insert into tbl_scan_trans (id,orderNum,respCode,merId,transAmt,transStatus,transType,chanMerId,chanCode,chanRespCode,"
        "createTime,updateTime,createTm,updateTm,refundStatus,refundAmt,fee,netFee,tradeFrom,lockFlag,settRole,payTime,currency,"
        "busicd,convertTransCode,agentCode,terminalid,discountAmt,sysTime,acqSponsor,signedSettleAmt,merFee,clearFlag,transMode)"
        "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',"
        "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        '34'+str(i), '15233582'+str(i), '00', '000290458120001', 22.78, '00', 1, '2088711569682939', 'ALP', 'SUCCESS',
        '2019-02-11 11:08:20', '2019-02-11 11:08:21',
        '2019-01-12 11:08:20', '2019-01-12 11:08:21', 0, 0, 1, 0, 'openapi', 0, 'ALP', '2019-02-04 11:08:20', 'CNY',
        'PURC', 'BPA', '00000045',
        '10000001', 0, '2019-03-08 16:04:44.225', '00000045', 22.78, 22.78, 0, 1))

# cursor.execute("insert into tbl_scan_trans (id,orderNum,respCode,merId,transAmt,transStatus,transType,chanMerId,chanCode,chanRespCode,"
#                "createTime,updateTime,createTm,updateTm,refundStatus,refundAmt,fee,netFee,tradeFrom,lockFlag,settRole,payTime,currency,"
#                "busicd,convertTransCode,agentCode,terminalid,discountAmt,sysTime,acqSponsor,signedSettleAmt,merFee,clearFlag,transMode)"
#                "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',"
#                "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%('222','15233582340','00','000290458120001',20302.78,'00',1,'2088711569682939','ALP','SUCCESS','2019-02-19 11:08:20','2019-02-19 11:08:21',
#     '2019-01-12 11:08:20','2019-01-12 11:08:21',0,0,1,0,'openapi',0,'ALP','2019-02-04 11:08:20','CNY','PURC','BPA','00000045',
#     '10000001',0,'2019-03-08 16:04:44.225','00000045',20302.78,20302.78,0,1))

db.commit()