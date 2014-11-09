#!/usr/local/bin/python27
import function

print '{:>30}'.format('right aligned')

print function.getstr()

f = open('string.py','r')
str =f.read()
str = 'name : %s'
print str % ('huang')
