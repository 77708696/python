#!/usr/local/bin/python27
import my_config
import sys,MySQLdb,time


#conn=MySQLdb.connect(host,user="root",passwd="123456",db="",charset="utf8") 

conn=MySQLdb.connect(my_config.host,user="root",passwd="123456",db="",charset="utf8")
conn.select_db("test") #switch database
cursor = conn.cursor()

f = open('/root/test.sql','r')
i = 0
for astr in f.read().split(';'):
    #
    if len(astr)>5:
        print astr
        i=i+1
        print "index:%s ,len: %s" % (i,len(astr))
        cursor.execute(astr)

f.close()
cursor.close()
conn.close()
