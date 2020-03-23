file =open("c:\\temp\\result.txt","r")  #r read

content=file.read()
print(content)

file.close()

with open("c:\\temp\\result.txt","r") as file:
    content = file.read()
    print(content)

with open("c:\\temp\\result.txt","r") as file:
    for line in file:
        print(line)


file =open("c:\\temp\\result.txt","r")  #r read

fragment=file.read(10)
while fragment:
    print(file.tell(),fragment)
    fragment=file.read(10)

file.close()

filename= 'c:\\temp\\output.txt'
line='urope'
cities=['london','Berlin','paris',"warsaw"]
file = open(filename,'a')           # jesli dopisac to "a"   w+ zapis i odczyt   a+ zapis i occzyt z zachowaniem zawartosci
file.write(line)
file.write('\n')
#file.writelines(cities)
for city in cities:
    file.write(city+'\n')

file.close()