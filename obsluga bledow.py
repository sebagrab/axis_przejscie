import sys
taskPerPerson=0
try:
    tasks=32
    personStr= input("hom many person are there in the team??")
    person=int(personStr)
    taskPerPerson=tasks / person

except ValueError:
    print("sorry you need to enter an integar number")
except ZeroDivisionError as e:
    print("Sorry - 0 isnt team",e)
except:
    print("somthing went wrong...",sys.exc_info()[0])
else:   #jesli nie doszlo do zadnego bledu
    print("every person shoud have around",taskPerPerson,"task")
finally: # wykonane nawet jesli jest blad jakis
    print("skonczona instrukcja")
