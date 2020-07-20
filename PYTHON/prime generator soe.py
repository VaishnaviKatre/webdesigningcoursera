def soe(n):
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <=n): 
        if (prime[p] == True):
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime

t=int(input("Enter no of test cases :"))
if t<=10:
    while(t!=0):
   
        m=int(input("Enter first no : "))
        n=int(input("Enter last no : "))
        prime=soe(n)
    
        if m>=1 and n<=1000000000 and n-m<=100000:
            if m==1:
                x=2
            else:
                x=m
            for i in range(x,n+1):
                if(prime[i]):
                    print(i, end=" ")
        else :
            print("Invalid input ")
        t-=1
 