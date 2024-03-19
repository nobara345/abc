# ATM File Handling

def readPin():
    file = open("pin.txt","r")
    a = int(file.read())
    file.close()
    return a

def readBal():
    file = open("bal.txt","r")
    a = int(file.read())
    file.close()
    return  a

def writePin(a):
    file = open("pin.txt","w")
    file.write(f"{a}")
    file.close()

def writeBal(a):
    file = open("bal.txt","w")
    file.write(f"{a}")
    file.close()
    print("press 1 : withdraw")
    print("press 2 : Check balance")
    print("press 3 : Change pin ")
    print("press 4 : Deposit")
choice = int(input("enter your choice = "))

if(choice==1):
    upin = int(input("enter a pin = "))
    if(upin==a):
        amount = int(input("Enter a amount = "))
        
