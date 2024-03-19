# with argument with return
def div(a,b):
    ans = a / b
    return ans

a = div(25,5)
print(a)

# with argument without return
def div(a,b):
    ans = a / b
    print(ans)

div(25,5)



# without argument with return

def div():
    a = 25
    b = 5
    ans = a / b
    return  ans

a = div()
print(a)



# without argument without return

def div():
    a = 25
    b = 5
    ans = a / b
    print(ans)

div()