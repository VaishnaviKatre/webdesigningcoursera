from math import *
              
def ssoe(m,n,nums): 
    nums[0]=0
    for i in range(0,floor(sqrt(n))):
        if nums[i] != 0:
            j=2
            while(nums[i]*j <=n ):
                nums[nums[i]*j-1]=0
                j=j+1

    for i in range(m-1,n):
        if nums[i] != 0 and m<= i+1 <=n :
            print(i+1)
    

t=int(input(""))
while(t != 0):
    m,n=[int(x) for x in input().split(" ")]
    nums=[x for x in range(1,n+1)]
    ssoe(m,n,nums)
    t=t-1
    print('')