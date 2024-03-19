print("GUESS THE NUMBER")
import random

num = random.randint(1,8)
guess=int(input("Enter your number: "))
if(num==guess):
    print("you win")
elif(num>guess):
    print("the number is smaller")
else:
    print("the number is greater")
print("the number was:", num)