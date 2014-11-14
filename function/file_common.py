def openfile(name):
    filetext = '';
    with open(name,"r") as f:
        filetext = f.read()
    return filetext

