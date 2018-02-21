class __task1():
    Nu = []
    St = []
    
    for i in range (0,5):
        print("type number")
        Nu.append(input())
    for j in range (0,5):
       print("type string")
       St.append(input())
       
def f(Nu): 
    res = 0
    for h in range (0,5):
        res = res + Nu[h]
    print(res)
def u(St):
    for h in range (0,5):
        print (St[h][::-1])
        
class __task2():
    Y="y"
    while len(Y) > 50 or len(Y)<30:
        print("input")
        Y= str(input())
        textoutput=open("textfile.txt","w") 
        textoutput.write(Y)
        textoutput=open("textfile.txt","r") 
        print(textoutput.read())
        textoutput.close
        
       