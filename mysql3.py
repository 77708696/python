#!/usr/local/bin/python27
#from string import Template
#import Template

'''
install 
tar -xzvf MySQL-python-1.2.4b4.tar.gz 
cd MySQL-python-1.2.4b4
 python27 setup.py install
whereis  mysql_config
ls /usr/local/bin/
find /usr -name mysql_config
vim site.cfg 
python27 setup.py install
find /usr -name libmysqlclient.so.18
ln -s /usr/local/mysql/lib/libmysqlclient.so.18 /usr/lib/libmysqlclient.so.18
ln -s /usr/local/mysql/lib/libmysqlclient.so.18 /usr/local/lib/libmysqlclient.so.18
ldconfig

'''
import sys,MySQLdb,time


print(sys.prefix)
print(time.time())

conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="testdb",charset="utf8")
cursor = conn.cursor(MySQLdb.cursors.DictCursor) 

cursor.close()
conn.close()