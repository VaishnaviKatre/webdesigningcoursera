import math
m=int(input("Enter the first number : "))
n=int(input("Enter the last number : "))
primes = []
for i in range(m,n+1):
    primes.append(i)

i = 2
while(i <= int(math.sqrt(n))):
    if i in primes:
        for j in range(i*2, n+1, i):
            if j in primes:
                primes.remove(j)
    i = i+1

print (primes)
