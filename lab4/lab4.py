class __Task1():
    tot = 0
    res = 0
    course=[]
    grades = []
    student=[]
    print("enter name")
    Name = input()
    print("enter age")
    age = int(input())
    student = [Name,age]
    print("enter number of courses")
    numberofcourses = int(input())
    for i in range(1, numberofcourses+1):
        print("enter name of course n°",i)
        A=input()
        student.append(A)
        print("enter number of grades in course n°",i)
        numberofgrades=int(input())
        tot = 0
        res = 0
        for j in range(1, numberofgrades+1):
            print("enter grade",j," of course n°",i)
            B=float(input())
            student.append(B)
            tot = tot + B
        res = tot/j
        print(A,res)
        
        

class __Task2():
    Stores=[]
    cheap = []
    print("enter number of store")
    Z = int(input())
    for g in range(1,Z+1):
        print("enter name of store",g)
        Y = [input()]
        Q= str(Y)
        Stores.append(Y)
        print("enter number of items")
        A=int(input())
        for i in range(1,A+1):
            print("enter name of the item",i)
            B=input()
            print("enter price of the item",i)
            C=float(input())
            if C <10:
                cheap.append([Q,B,C])
                cheap.sort(key=lambda x: x[2])
                Y.append([B,C])
            else:
              Y.append([B,C])

    print(cheap)
            
class __Task3():
    li=[]
    for i in range(0, 5):
        print("enter a string")
        Z=str(input())
        li.append(Z)
    print(li)
    print("type previously entered list")
    Y=str(input())
    for i in range(0,4):
        if str(li[i])==Y:
            del li[i]
    print(li)
    print("enter string")  
    F = str(input()) 
    li = [F]+li
    print(li)
    for l in range (0,4):
        if len(str(li[l]).split()) >1:
            for x in str(li[l]).split():
                print (x)
    print("type a string")
    X=str(input())
    S= X[::-1]
    print(S)
            
    
               
      
        