import os, string

def rename():
    cwd = os.getcwd()
    path = cwd + '\images'
    fList = os.listdir(path)
    
    os.chdir(path)
    for file in fList:
        trans = file.maketrans('', '', string.digits)
        print('Renamed %s to %s' % (file, file.translate(trans)))
        os.rename(file, file.translate(trans))

    os.chdir(cwd)
rename()
