# a=input("what is your name:\n")
# b=input("how much do you earn: ")
# if int(b)==0:
#     raise ZeroDivisionError("B is 0 so stoping he program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"Hello! dear {a}")
# # 1000 lines taking 1 hour

# task.......write about 2 built in exceptions


c = input("enter your name:\n ")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("harry is blocked, he is not allowed")
    print(" Exception handled")
