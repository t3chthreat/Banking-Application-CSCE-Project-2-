#CSCE Project #2 
print("+----------------------------------------------------+")
print("|      Computer Science and Engineering              | ")
print("|     CSCE 1035.001 - Computer Programming I         | ")
print("|  Jonathan Chen  jec0412  joanthanchen3@my.unt.edu  | ")
print("+----------------------------------------------------+ ")
#Banking app 
from enum import Flag
import sys
from tkinter import N, Y
from unittest import expectedFailure


#setting the paramaters 
balance = 0.0
login_data = {}
flag = 0 


# setting up the password encryption rules
def encrypt(password):
    l = list(password)

    for c in range(len(l)):
        m = ord(l[c])
        if 97 <= m <= 122:
            l[c] = chr((m + 3 - 97) % 26 + 97)
        elif 65 <= m <= 90:
            l[c] = chr((m + 3 - 65) % 26 + 65)
        elif 48 <= m <= 57:
            l[c] = chr((m + 3 - 48) % 10 + 48)
            continue
    return "".join(l)


#intial User ID credential set up 
username = str(input("Enter New Banking ID:"))
password = str(input("Enter password:"))
balance = float(input("Enter Intial Balance:"))
login_data[2] = encrypt(password)
login_data[1] = username 
login_data[username] = encrypt(password)



#setting up the login rules 
def login():
    global flag
    if flag == 1:
        print("+----------------------------------------------------+")
        print("|             USER IS ALREADY LOGGED IN              | ")
        print("+----------------------------------------------------+ ")
    else:
        username = str(input("Enter username:"))
        password = str(input("Enter password:"))
        if username == login_data[1]:
            password == login_data[2]
            flag = 1 
            print("+----------------------------------------------------+")
            print("|                  LOGIN SUCCESSFUL                  | ")
            print("+----------------------------------------------------+\n")
        elif username != login_data[1]:
            print("+----------------------------------------------------+")
            print("|                  LOGIN  FAILED                     | ")
            print("|              INCORRECT    USER ID                  | ")
            print("+----------------------------------------------------+\n")
        elif password != login_data[2]:
            print("+----------------------------------------------------+")
            print("|                  LOGIN  FAILED                     | ")
            print("|             INCORRECT     PASSWORD                 | ")
            print("+----------------------------------------------------+\n")


#setting the paramaters for withdrawl functions 

def withdrawal():
    global balance

    if flag == 0:
        print("+----------------------------------------------------+")
        print("|             USER IS NOT LOGGED IN                  | ")
        print("+----------------------------------------------------+ ")
    else:
        amount = input("Enter the withdrawal amount:")
        if float(amount) > balance:
            print("+----------------------------------------------------+")
            print("|              TRANSACTION DELCINED                  |")
            print("|               INSUFFICENT FUNDS                    |")
            print("+----------------------------------------------------+")
        else:
            balance -= float(amount)
            print("+----------------------------------------------------+")
            print("|              TRANSACTION APPROVED                  |")
            print("|              WITHDRAWL SUCCESSFUL                  |")
            print("+----------------------------------------------------+")


#setting the paramaters for depositing functions
def deposit():
    global balance
    if flag == 0:
            print("+----------------------------------------------------+")
            print("|             USER IS NOT LOGGED IN                  |")
            print("+----------------------------------------------------+")
    else:
        amount = input("Enter amount to deposit:")
        balance += float(amount)
        print("+----------------------------------------------------+")
        print("|              TRANSACTION APPROVED                  |")
        print("|               DESPOSIT SUCCESSFUL                   |")
        print("+----------------------------------------------------+")


#allow for the user to change password 
def change_password():
    global flag
    if flag == 0:
        print("+----------------------------------------------------+")
        print("|             USER IS NOT LOGGED IN                  |")
        print("+----------------------------------------------------+")
    else:
        username = str(input('enter username :'))
        password = str(input("Enter new password:"))
        login_data[2] = encrypt(password)


#Banking app meanu
while (1):
    ch = int(input('+******** M E N U **********+\n| 1. Login                |\n| 2. Deposit to Account  |\n| 3. Withdrawal          |\n| 4. Balance             |\n| 5. Change Password     |\n| 6. Exit/Logout         |\n+***************************+\n Enter Choice->'))

    if ch == 1:
        login()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdrawal()
    elif ch == 4:
        print("+----------------------------------------------------+")
        print("|                 AVAILABLE  BALANCE                 |")
        print("|"                 '$' , balance , '$'                "|")
        print("+----------------------------------------------------+")
    elif ch == 5:
        change_password()
    elif ch == 6:
            flag = 0
            print(login_data[1],", has logged out.\n")
            print ("would you like to close this app?")
            end = input("Y/N:")
            if end == Y:
                flag = 0
                print("Thank you for banking with us have a nice day" )
                sys.exit()
            elif end == N:
                print("Please sign back in access you account information")
                continue
    elif ch == 9:
        print(login_data[1], login_data[2],"$",balance)
    else:
        print("+----------------------------------------------------+")
        print("|                INVALID  CHOICE                     |")
        print("|               PLEASE  TRY  AGAIN                   |")
        print("+----------------------------------------------------+")