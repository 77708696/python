
'''
http://bazaar.launchpad.net/~mkindahl/mysql-replicant-python/trunk/view/head:/lib/tests/test_config.py
'''
import sys,os.path,tempfile

rootpath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(rootpath)

__version_info__ = (0, 9, 0, '')
__version__ = '%d.%d.%d%s' % __version_info__

print(__version__)

print(os.path.abspath(__file__))
print(__file__)

filename = __file__;
dirname = os.path.dirname ( os.path.abspath(__file__) ) 
print( dirname )



print('---------------')
print(os.path.join(dirname,filename))

print(tempfile.mkstemp(text=True)[1])