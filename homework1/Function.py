import matplotlib.pyplot as plt

class homework(object):
    

    print("enter A value")
    A = float(input()) 
    print("enter M value")
    M = float(input())
    print("enter H value")
    H = float(input())


    values = []
    returnvalues = []
    i=0
    def f(x) : return (2+x)*(x+(1/x))/(x*x*(1/(1+x*x)))

    if H <= 0:        
        print("wrong H value")        
    else:
        while f(A + i*H) < M and i < 14:                    
            V = f(A + i*H)  
            if V != float("inf") or V != float("-inf") or not isinstance(V,float) :
               returnvalues.append(V)  
               values.append(A + i*H)
               i = i+1         
            else: 
                print("not available")
                i = i+1 
    print(returnvalues)
    plt.plot(values,returnvalues)
    plt.show()
