import time

class lab3: 
   
    
    A = float(time.strftime("%d"))
    B = float(time.strftime("%m"))
    C = float(time.strftime("%Y"))




    print("enter birthday day eg 26")
    day = float(input())
    print("enter birthday month eg 09")
    month = float(input())
    print("enter birth year eg 1983")
    year = float(input())

   
    
    daysinayear = float(365.2425)
    
    pedays = day+month*30+year*daysinayear
    curdays = A+B*30+C*daysinayear
    
    ageoftheperson = (curdays-pedays)/daysinayear #i could've done it in one line but itwould've been unclear
    
    print ("you are " ,ageoftheperson)
    
    if A == day and B == month :
        print("happy birthday")
    else:
        days1 = A + B*30
        days2 = day + month*30
        difference = abs(days1 - days2)
        print("your birthday is in " ,difference ,"days")

  