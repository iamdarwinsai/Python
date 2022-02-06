import getpass

a=str(input("Enter your Username: \n"))
key = getpass.getpass('Password :: ')
if key == 'joey':
    print("LOgged In Successfully")
    print("Welcome "+a+" "+"Please select the options below: \n")
    print(''' 
        1.Balance Enquiry
        2.Cash Withdrawal
        3.Change Pin
        4.Bank statement

        ''')
    Options = int(input("Choose your option : \n"))
    if Options == 1:
        n=int(input("Enter your ATM pin: \n"))
        print("ATM PIN IS CORRECT")
        print("Amount present in your bank is RS.50000 INR") 
    elif Options == 2:
        n=int(input("Enter your ATM pin: \n"))
        print("ATM PIN IS CORRECT")
        With = int(input("Enter the withdrwal amount: \n"))
        if With > 50000 :
            print("Amount is Greater than your aukat")
        else :
            print(f"{With} amount sucessfully withdrawal")
    elif Options == 3 :
        n=int(input("Enter your new pin: \n"))
        np=int(input("Enter your new pin: \n"))
        print(f"Pin changed to {np} Scessfully")
    else:
        n=int(input("Enter your new pin: \n"))
        print('''
        Amount Present in your bank : RS.50000
        Last Logged in : Yesterday
        IP : 127.10.10.01
        ''')
    print("Thankyou for using Xploit3r Bank")

else:
    print("Wrong PAssword")




