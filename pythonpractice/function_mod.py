# with argument with return
def mod(a,b):
    ans = a % b
    return ans

a = mod(25,5)
print(a)

# with argument without return
def mod(a,b):
    ans = a % b
    print(ans)

mod(25,5)



# without argument with return

def mod():
    a = 25
    b = 5
    ans = a % b
    return  ans

a = mod()
print(a)



# without argument without return

def mod():
    a = 25
    b = 5
    ans = a % b
    print(ans)

mod()