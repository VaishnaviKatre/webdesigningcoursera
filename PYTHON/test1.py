t=int(input("Enter the number of test case :"))
if t<=10:
    for i in range(0,t):
        x=int(input("enter first number :"))
        y=int(input("Enter last number :"))
        if x>=1 and y<=1000000000 and y-x<=100000:
            if x==1:
                m=2
            else:
                m=x
            l=y
            n=l+1
            lst=[]
            lst1=[]
            lst2=[]
            count=0
            for i in range(m,n):
                lst.append(i)
            if 2 in lst:
                print(" ")
            else:
                for l in lst:
                    for i in range(2,m):
                        v=l%i
                        if v==0:
                            lst1.append(l)
            for p in lst:
                n=int(l/p)+1
                for i in range(2,n):
                    if p*i <=l and p*i not in lst1:
                        lst1.append(p*i)
            for i in lst:
                if i not in lst1:
                    lst2.append(i)
                    print(i)
        else:
            print("wrong input range!")

else:
    print("Enter test case number <=10!")