__author__ = 'huangxiaoming'
#https://github.com/PyMySQL/PyMySQL#resources 安装包
#导入pymysql的包  
import pymysql

try:  
#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库  
    conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='oradt_cloud',port=3306,charset='utf8') 
    cur=conn.cursor()#获取一个游标  
    cur.execute('select * from account_basic')  
    data=cur.fetchall()  
    for d in data :  
        #注意int类型需要使用str函数转义  
        print("ID: "+str(d[0])+'  名字： '+d[1]+"  性别： "+d[2])
        print(d)


    cur.execute("show tables")    
    data = cur.fetchall()
    for d in data:
        print(d)
    cur.close()#关闭游标  
    conn.close()#释放数据库资源  
except  Exception :print("发生异常") 