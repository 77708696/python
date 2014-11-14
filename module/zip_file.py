import zipfile


f = zipfile.ZipFile("a.zip", 'w', zipfile.ZIP_DEFLATED)
f.write("conn_fun.py")
f.close()