filename =input("ener filemame")

print ("the file mane is %s" %(filename))

while True:
    filesizestr=input("max file size (MB)")
    if filesizestr.isdecimal():
        filesizeint=int(filesizestr)
        break
print ("max size input%s"%(filesizeint))
print ("size in kb is %d" %(filesizeint*1024))




