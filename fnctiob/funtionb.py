"""a=9
b=8

c = sum((a,b))#built in function
print(c)"""


"""def function2():
    print("hello you are in function2")

(function1())"""
def average (a,b):
    """your in function2  which is usd to get average of two numbers"""
    average=(a+b)/2
    #print(average)
    return average
v = average(5,7)
print(v)
print(average.__doc__) # doc string