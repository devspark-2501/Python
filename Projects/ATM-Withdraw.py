# Project Idea: ATM Withdraw

Balance = float(input('Enter Your Balance: '))
Withdraw = float(input('Enter Amount To Withdraw: '))

if Withdraw < 0:
    print("Invalid Amount")
elif Balance >= Withdraw:
    Result = Balance - Withdraw
    print("Transaction Successful")
    print(f"Remaining Balance: {Result}")
else:
    print("Insufficient Balance")
print('Thank For Using us') # Extra Line