# Recursion

# def abc():
#     code
#     abc()
#
# abc()



# def hello():
#     print("Hello")
#     hello()
#
# hello()



# def hello(a):
#     if(a>0):
#         print("Hello")
#         a -= 1
#         hello(a)
#
# hello(5)


# ===============================

# 5! = 5x4x3x2x1 = 120
# 4! = 4x3x2x1
#
# 5! = 5x4!
#
# n! = n x (n-1)!

# 1! = 1
# 0! = 1
#==================================
# def fact(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         return num * fact(num-1)
#
# a = fact(984)
# print(a)

# =================================================

# default argument
def info(fname,lname,age=20):
    print("name = ",fname)
    print("lname = ",lname)
    print("age = ",age)

info("Anushka","kedar")

# here age value is fix/default