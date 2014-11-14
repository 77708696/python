import getopt

agrv = '-a -b -cfoo -d bar a1 a2'.split()
optlist, args = getopt.getopt(agrv, 'abc:d:')

print(optlist)
print(args)