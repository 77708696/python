
#http://blog.csdn.net/wudiyi815/article/details/7775549
a = (1,3,2,7,1)
b = list(a)
print(b)
b.sort()

print( 10 in b)

a = tuple(b)
print(a)

print(b.index(1))


tlist = ({'host':'192.168.30.191','user':'root'},{'host':'192.168.30.192','user':'root'})

for tdata in tlist:
    print("ip:%s user:%s" % (tdata['host'],tdata['user']))