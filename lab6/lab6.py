##TASK1
i= int
j= int
x=0
y=0
som = []

def algorithm() :
       print("select n")
       n = int(input())
       if (0<=n<=10) :
           print("select m")
           m= int(input())
           if  (0<=m<=10):
               A = [[0 for x in range(n)] for y in range(m)] 
               for i in range(0,n):
                for j in range (0,m):
                    print("enter element","[",i,"]","[",j,"]")
                    A[i][j] = int(input())  
               for h in range (0,min(m,7)):
                  som.append(0)
                  for g in range (0 , n):
                       som[h] = som[h] + A[g][h] 
           return A,som         
           
     ##  i don't really get the second question 
     ##,if it is asked to return only the negative 
     ##sums here is the code :
     
     ##if som[h] < 0 listofnegativesums.append(som[h]):
     ##  return listofnegativesums
     
     ##maybe it is about returning a sum
     ##of only negative elemtents from the rows 
     ##in which case here is the solution:
     
     ##for h in range (0,min(m,7)):
     ##            som.append(0)
     ##             for g in range (0 , n):
     ##                 if A[g][h] < 0 :
     ##                  som[h] = som[h] + A[g][h] 
     ##      return A,som   
     
##TASK2
def banknotes():
     print("enter S")
     S = int(input())
     print("enter number of different Bij")
     NbBij = int(input())
     B = []
     for l in range(NbBij):
         print("enter Bij size",l)
         Bijsize = int(input())
         B.append([Bijsize])
         print("enter number of Bij",Bijsize)
         NbofBij = int(input())
         B[l].append(NbofBij)
     return B
         
     ## the question 3 is a complex mathematical problem i have no idea 
     ##how to resolve,the python implementation would be easier though