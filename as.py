from pathlib import Path
import datetime
import os
import datetime
import shutil
print("hello")
print('2+2')
zmienna=1
inna=2
ala=zmienna+inna
print(ala)
print(zmienna.bit_length())
slowo="kot"
print(slowo.isupper())
print(slowo.upper())
print(slowo.isupper())
print(slowo.lower())
print(slowo[2])
print(slowo.find("o"))

txt = Path('C:\\Users\\grabowss\\Desktop\\IP_MKwiag.txt').read_text()
print(txt.find('17'))
k = txt.find("17")
print(k)
print(txt[k+3:k+11])
fileName=datetime.datetime.now()
def create_file():
    with open(fileName.strftime("%d %B %Y %H")+"ala"+".txt", "w") as file:
        file.write("dupa")

create_file()


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

d = modification_date('C:\\Users\\grabowss\\Desktop\\aaa.txt')

print (d)
e = modification_date('C:\\Users\\grabowss\\Desktop\\aa.txt')

print (e)
if d > e:
    print("porównanie ok")
    shutil.copyfile('C:\\Users\\grabowss\\Desktop\\IP_MKwiag.txt','C:\\Users\\grabowss\\Desktop\\A\\IP_MKwiag.txt')
    k=1
while e > d:
    print("ok")
    txt = Path('C:\\Users\\grabowss\\Desktop\\aa.txt').read_text()
    file = open('C:\\Users\\grabowss\\Desktop\\aa.txt','w')
    file.write(txt+'\r\n')
    k=k+1
    file.write(str(k))
    file.write(fileName.strftime(" %H %M %S"))
    file.close()
    fileName = datetime.datetime.now()

    print('dupa'
          )
