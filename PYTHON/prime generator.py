import math
def checkprime(num) :

    if num <=1:
        return bool(0)
    elif num == 2 :       
        return bool(num)
    elif num % 2 == 0:
        return bool(0)
    else:
        prime = True
        divisor = 3
        upperLimit =math.sqrt(num) +1
        while divisor <= upperLimit:
            if num % divisor == 0:
                return False;
            divisor +=2;
        return prime;
    
t=int(input("Enter no of test case less than or equal to 10 : "))
while t!=0:

    if t<=10:
        m=int(input("Enter first number :"))
        n=int(input("Enter last number :"))
        if m>=1 and n<=1000000000 and n-m<=100000:
            for j in range (m,n+1):
                if checkprime(j):
                    print(j)
        else:
            print("Invalid input")
    else :
        print("Not in range ")
    t-=1