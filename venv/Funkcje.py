def Printel():
    #drukuje hello
    print("hello")
    return

Printel()
Printel()
Printel()
Printel()

def workingday(years,month=1,day=1):      #1 parametr domyslny jesli nic nie wpisane
    from datetime import date
    from datetime import timedelta

   # day=date.today()
    day=date(years,month,day)
    if day.weekday()==5:
        workingday = day+ timedelta(days=2)
    elif day.weekday()==6:
        workingday = day + timedelta(days=1)
    else:
        workingday=day
   # print ('working day for',day,'is',workingday)
    return workingday

workingday(2017,2)

nextworkingday=workingday(2020,3,15)
print(nextworkingday)

def Action(action,parametr):
    print("action",action)
    print("parametr",parametr)
    return

Action('buy','shoes')


def Action2(action,*parametr):
    print("action",action)
    print("parametr",parametr)
    for element in parametr:
        print("element is ",element)
    return
Action2('buy','shoes',"cocks")


def Action3(action,what,**parametr):
    print("action",action)
    print("what",what)
    print("parametr",parametr)
    for element in parametr:
        print(element,'=',parametr[element])
    return

Action3('buy','shoes',size=45,color='brown',type='sport')

def weekday(dayNumber):
    names={
        0: "poniedzialek",
        1: "wtorek",
        2: "sroda",
        3: "czwartek",
        4: "piatek"
    }
    return names.get(dayNumber,"error")

print(weekday(2))