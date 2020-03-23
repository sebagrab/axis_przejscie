import os
import time

print("current directory is",os.getcwd())

currentDir=os.getcwd()
filename='result.txt'
fullpath=os.path.join(currentDir,filename)
print('constructed file path is ',fullpath)

relativePath="output.txt"
print("the absolute path is",os.path.abspath(relativePath))

filePath = r'c:\temp\result.txt'
print("filename part is ",os.path.basename(filePath))
print('directory path is ',os.path.dirname(filePath))
print('is file existing',os.path.exists(filePath))

if os.path.exists(filePath):
    print('las modyfy date is',os.path.getmtime(filePath))      #data modyfikacji mozna tez data utworzenia
    print(("last modifity date is",time.localtime(os.path.getmtime(filePath))))

    print ("file size is",os.path.getsize(filePath))

    print("is it a file ",os.path.isfile(filePath))
    print("it is a dir", os.path.isdir(filePath))

    print("path spilted",os.path.split(filePath))
    print("only file name part",os.path.split(filePath)[1])

    print("path spiltted into drive",os.path.splitdrive(filePath))
    print("only drive",os.path.splitdrive(filePath)[0])
while not fileIsOk:
    filename = input("enter path to results file")
    if os.path.isfile(filename):
        break
    else:
        print("niepoprawna sciezka")
print ("the result file is %s" %(filename))
