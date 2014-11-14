import sys,getopt

print(sys.argv)
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
print(args)
for i in range(0,len(sys.argv)):
    print(sys.argv[i])



