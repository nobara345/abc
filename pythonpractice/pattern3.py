# 1 1 1 1 1
# 0 1 1 1 1
# 0 0 1 1 1
# 0 0 0 1 1
# 0 0 0 0 1

for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()