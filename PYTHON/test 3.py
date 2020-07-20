# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:27:58 2020

@author: vaishnavi
"""

list=[]
t=int(input("Enter the number of cases:"))
for l in range(0,t):
    a=eval(input("Enter the lower and upper limit:"))
    list.append(a)
for i in range(0,t):
    m=list[i][0]
    n=list[i][1]
    for j in range(m,n+1):
        h=0
        for k in range(1,j+1):
            if j%k==0:
                h=h+1
        if h==2:
            print(j)