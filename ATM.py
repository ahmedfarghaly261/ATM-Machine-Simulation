print("enter your card ")
password=1234
pin=int(input("enter your password : "))

if pin==password:
    while True:
        balance=5000
        print("welcome")
        print("""
            1==current balance
            2==Cash withdrawal
            3==Cash deposit
            4==change pin
            5==exit
            """)
        #current balance = 5000
        option=int(input("enter number from the list : "))
        if option==1:
            print(f"balance = {balance}")
            
        #cash withdrawal 
        if option ==2:
            amount=int(input("enter the withdraw amount : "))
            if amount>balance:
                print("the amount is grater than balance")
                break
            else:
                balance=balance-amount
                print(f"{amount} is debited from your account")
                print(f"your current account balance is : {balance}")
            
        #cash deposit
        if option == 3:
            CashDeposit=int(input("enter the Cash deposit : "))
            balance=balance+CashDeposit
            print(f"your current balance is : {balance}")
            
        #change password
        if option ==4:
            print("change your password! ")
            oldPassword=int(input("enter the old password"))
            if oldPassword==password:
                newpassword=int(input("enter your new password"))
                password=newpassword
                print(f"done  your new password is : {password}")
            else:
                print("incorrect password")
                break
            
        #exit
        if option==5:
            break
            
else:
    print("incorrect password .... try again")

