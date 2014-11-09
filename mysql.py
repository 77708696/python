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

class Point(object):
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

#s = Template('$who likes $what')
#print s.substitute(who='tim', what='kung pao')

print '{0}, {1}, {2}'.format('a', 'b', 'c')

print sys.prefix
print time.time()

conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="test",charset="utf8")
cursor = conn.cursor(MySQLdb.cursors.DictCursor)    
sql = "insert into t (name,id) values (%s,12)"   
param = (("aaa"),("aaa"),("aaa")) 
n = cursor.executemany(sql,param)    
print n
cursor.execute("""insert into t(name,id) values ('huang',23);""")
#cursor.execute("""create database python """)
cursor.execute('select * from t;')
for data in cursor.fetchall():
    print data 
'''
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20) | NO   |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)


'''
sql = "insert into t2 (name) values (%s)"   
param = (("aaa"),("cc"),("dd")) 
#n = cursor.executemany(sql,param)
'''python not autocommit    '''
conn.commit()
lines = cursor.execute('select * from t2')
for data in cursor.fetchall():
    print "id: %s , name: %s " % (data['id'],data['name'])

cursor.close()

conn.close()   
