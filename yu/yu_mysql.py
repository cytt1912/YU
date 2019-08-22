import pymysql

db = pymysql.connect("localhost","db","db","db")
for i in range(10000):
    cursor.execute(
        "insert into table1(id,orderNum)VALUES ('%s','%s')" % (
        '34'+str(i), '15233582'+str(i)))
db.commit()