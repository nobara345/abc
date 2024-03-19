# with argument with return
def sub(a,b):
    ans = a - b
    return ans

a = sub(30,20)
print(a)

# with argument without return
def sub(a,b):
    ans = a - b
    print(ans)

sub(30,20)



# without argument with return

def sub():
    a = 30
    b = 20
    ans = a - b
    return  ans

a = sub()
print(a)



# without argument without return

def sub():
    a = 30
    b = 20
    ans = a -b 
    print(ans)

sub()