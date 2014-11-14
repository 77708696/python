
'''

pyton 测试

install redis 
https://pypi.python.org/pypi/redis/2.10.3

'''

import Myconfig
import redis;
import time

r = redis.StrictRedis(host=Myconfig.redis_host,port=Myconfig.redis_port,db=0)
'''
r.set("test_01","test_1")
str1 = r.get("test_01")
print("value=%s" % (str1.decode()) )
print(type(str1))
'''
i=0
while 1==1:
    print(i)
    i=i+1
    time.sleep(1)
    strtime = time.time()    
    print( str(strtime).split('.'))
    print( int(time.time()) )
    r.set(("key_%s"%(int(time.time()))),str(time.time()))
    
    
    
    

