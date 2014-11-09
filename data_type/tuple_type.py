#!/usr/local/bin/python27

import string

v=('a',1)

print v


(a,b) = v

print "a=%s %s" % (a,b)

s1 = '${a},like ${b}'
s = string.Template(s1)


dict = {'a':1,'b':'hello word!'}

print s.substitute(dict)