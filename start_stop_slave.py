import pymysql
try:

    conn=pymysql.connect(host='192.168.30.101',user='root',passwd='123456',db='test',
        port=3306,charset='utf8')
    '''conn.cursor 默认是获取列表，字典需要传参
                 pymysql.cursors.DictCursor
                 MySQLdb.cursors.DictCursor 
    '''

    cur=conn.cursor(pymysql.cursors.DictCursor)#获取一个游标 

    print("连接成功")

    cur.execute("show slave status")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.execute("start slave")
    cur.close()
    conn.close();

except Exception : print('mysql connection error')