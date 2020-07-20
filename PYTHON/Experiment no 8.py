class atm:


    def accinfo(self,name):
        print("Account details:")
		print('Name:',self.user[name]['Name'])
		print('Account:',self.user[name]['Account'])
		print('Mobile:',self.user[name]['Mobile'])
		print('Balance:',self.user[name]['Balance'])
        
    def pinchange(self,name):
        pin=int(input("Enter pin:"))
        i=3
        if pin==self.user[name]['Pin']:
            print("Pin matched.")
            ch=input("Press Y to change pin else, press N.")
            if ch=="Y" or ch=="y":
                pin=int(input("Enter new pin:"))
                pin=self.user[name]['Pin']
            elif ch=="N" or ch=="n":
                print("Process continuing..")
            else:
                print("Wrong key entered.")
        else:
            i=i-1
            print("Pin incorrect.")
            if i==0:
                print(i," attempts left.")
                print("CARD BLOCKED!")
            else:
                print(i," attempts left.")
                
    def balance(self,name):
        bal=input("Press Y to check balance else, press N.")
        if bal=="Y" or bal=="y":
            print("Your account balance is: Rs.",self.user[name]['Balance'])
        elif bal=="N" or bal=="n":
            print("Process continuing..")
        else:
            print("Wrong key entered.")
        
    def withdrawal(self,name):
        wd=input("Press Y to withdraw money else, press N.")
        n=self.user[name]['Balance']
        if wd=="Y" or wd=="y":
            m=int(input("Enter amount to be withdrawn: "))
            n=n-m
            print("Balance remaining: Rs. ",n)
        elif wd=="N" or wd=="n":
            print("Process continuing..")
        else:
            print("Wrong key entered.")

    def deposit(self,name):
        dp=input("Press Y to deposit money else, press N.")
        n=self.user[name]['Balance']
        if dp=="Y" or dp=="y":
            m=int(input("Enter amount to deposit: "))
            n=n+m
            print("Balance remaining: Rs. ",n)
        elif dp=="N" or dp=="n":
            print("Process continuing..")
        else:
            print("Wrong key entered.")
                
	users = {'Vaishnavi':{'Pin':'5005','Account':12435,'Mobile':9132458657,'Balance':100000},
		'Geetika':{'Pin':'4004','Account':17643,'Mobile':9243564782,'Balance':200000},
		'Raju':{'Pin':'3003','Account':14567,'Mobile':9543673456,'Balance':300000},
		'Sunita':{'Pin':'2002','Account':11287,'Mobile':9164367894,'Balance':400000},
		'Dada':{'Pin':'1001','Account':12875,'Mobile':7564829457,'Balance':500000}}
k=user.keys()

while (1):
    name=input('Enter Name: ')
    a=atm()
    if name in k:
        print('Enter 1 For Account Info')
        print('Enter 2 For PIN Change')
        print('Enter 3 For Balance Inquiry')
        print('Enter 4 For Withdrawal')
        print('Enter 5 For Deposit')
        s=int(input('Select Operation: '))
        if s==1:
            a.accinfo(name)
        elif s==2:
            a.pinchange(name)
        elif s==3:
            a.balance(name)
        elif s==4:
            a.withdrawal(name)
        elif s==5:
            a.deposit(name)
        else:
            print('Invalid Option Selected! Choose Again')
            continue
        e=input('Enter 0 to exit, press any other key to continue operations: ')
        if e==0:
            print('Thank You!')
            break
        else:
            continue
        break
    break