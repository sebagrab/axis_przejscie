l_mala = 3.14153456623
l_duza = 3.876464434342

print (l_duza,l_mala)
print(int(l_mala), int(l_duza))
print(abs(l_mala), abs(-l_mala))    # wartosc bezwzgledna
print(round(l_mala,2),round(l_duza,2))
print(min(l_duza,l_mala),max(l_duza,l_mala))

list=[1,2,3,4,5,6,3,4,3,4]

print(sum(list), len(list))
print(sum(list)/len(list))

print (round(2.444,2))

percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
             'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
             'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
             'Cyprus', 'Italy']

sumOfPoints= 4988

print(min(percent),max(percent))
temp=0
for temp in range(len(countries)):
    print(percent[temp],int(percent[temp]),round(percent[temp]))
    print((sumOfPoints*percent[temp])/100, 'głosów')
    print(countries[temp])
    temp=temp+1


import math     #nowy katalog w module
from math import *   #wszystkie funkcje w nowym katalogu


print(math.ceil(l_mala))    # najmniejsza liczba całkowita wieksza od tej liczby
print(math.floor(l_mala))   # najwieksza liczba calkowita wieksza od tej
print(pow(2,8),pow(9,0.5))  #potegowanie
print(math.sqrt(16))        #pierwiastek kwadratowy
print(math.pi, math.e)      #zmienne pi i e
print(math.sin(math.pi/2))      #sin

math_ls = dir(math)
print(math_ls)

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r ** 2
big_area = math.pi * big_pizza_r ** 2
family_area = math.pi * family_pizza_r ** 2

print('small', small_pizza_r, small_pizza_price, small_area)
print('big', big_pizza_r, big_pizza_price, big_area)
print('family', family_pizza_r, family_pizza_price, family_area)
print('')
print('small', small_pizza_price / small_area)
print('big', big_pizza_price / big_area)
print('family', family_pizza_price / family_area)
print('')


import random

print('one random numer ',random.randint(1,100))
print('choosing rundom number from a range',random.choice(range(1,100))) #jedna wartosc z listy
print('chosing rundom number from a range -easier', random.randrange(1,100))    #wartosc z listy
list=['john','ann','peter','susan','greg']
random.shuffle(list)                                                        #losowe mieszanie listy
print('reordered list', list)
print('just a random float', random.random())


#for i in range(32,127):
 #   print(i,chr(i))

ints = range(33,127)
password = ''
for i in range (16):
     password+= chr(random.choice(ints))
print('password is ',password)



