# with argument with return
def multi(a,b):
    ans = a * b
    return ans

a = multi(3,2)
print(a)

# with argument without return
def multi(a,b):
    ans = a * b
    print(ans)

multi(3,2)



# without argument with return

def multi():
    a = 3
    b = 2
    ans = a * b
    return  ans

a = multi()
print(a)



# without argument without return

def multi():
    a = 3
    b = 2
    ans = a * b
    print(ans)

multi()