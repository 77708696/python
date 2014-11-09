#!/usr/local/bin/python27

import glob


dir = glob.glob('/root/python/python/*.py')

for d in dir:
    print d
    #f = open(d,'r')
    #print f.read()
    #f.close()
