import os, string

def rename():
    path = r'C:\Users\Jarvis\OneDrive\Documents\Python\Programming Foundations with Python\images'
    fList = os.listdir(path)
    cwd = os.getcwd()
    
    os.chdir(path)
    for file in fList:
        trans = file.maketrans('', '', string.digits)
        print('Renamed %s to %s' % (file, file.translate(trans)))
        os.rename(file, file.translate(trans))

    os.chdir(cwd)

rename()
