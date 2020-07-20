num=int(input("Enter Number between 0 to 1000: "))
if 0<=num<=1000:
    for a in range (1,num):
        for b in range (a,num):
            if (a*a) + (b*b) == num:
                print([a,b])
else:
    print("Invalid Input")