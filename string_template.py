#!/usr/local/bin/python27
import function

print '{:>30}'.format('right aligned')

print function.getstr()
'''
f = open('string.py','r')
str =f.read()
'''
str = 'name : %s'

print str % ('huang')

a = 'name:haha,age:20|name:python,age:30|name:fef,age:55'



print a.split('|')
b = a.split('|')
for astr in b:
    print astr
