# Nested for loop

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(1,6):
    for j in range(1,11):
        print(j,end=" ")
    print()

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i}{j}",end=" ")
#     print()

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55

#
for i in range(1,6):
    for j in range(1,6):
        if(i==1):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# 1 1 1 1 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# =================================
for i in range(1,6):
    for j in range(1,6):
        if(i==j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

    # 1 0 0 0 0
    # 0 1 0 0 0
    # 0 0 1 0 0
    # 0 0 0 1 0
    # 0 0 0 0 1