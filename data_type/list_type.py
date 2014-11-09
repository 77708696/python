#!/usr/local/bin/python27

L = []

print 'type: %s' % (type(L))

L.append("aa")
L.append('huang')

L.insert(0,'xiaoming')

print "index0: %s \t L[0]: %s" % (L[0],L[1])

print L.pop()

print len(L)

for l in L:
	print l