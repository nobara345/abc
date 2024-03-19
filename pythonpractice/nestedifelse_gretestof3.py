a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
if a > b:
    if a > c:
        print("greatest number is:",a)
    else:
        print("greatest number is:",c)
else:
    if b > c:
        print("greatest number is:",b)
    else:
        print("greatest number is",c)