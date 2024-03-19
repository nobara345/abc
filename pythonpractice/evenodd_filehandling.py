file = open("xyz.py", "a")
file.write("""num = int(input("enter a number = "))\n""")
file.write("""if(num==0):\n    print("Even number")\n""")
a = 1
for i in range(1, 501):
    file.write (f"elif(num=={a}):\n" """  print("odd number")\n""")
    a+=1
    file.write(f"elif(num=={a}):\n""""  print("Even number")\n""")
    a+=1

file.write("""else:\n   print("Out of range")\n""")
file.close()