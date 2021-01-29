# Health  management system
#clients ="harry","Rohan","Hammed".
# total 6 files
def getdatetime():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for excercise and 2 for diet:\n"))
        if (c==1):
            value =input("Type here:\n")
            with open("Harry_ex.txt","a") as f:
                f.write(str([str(getdatetime())])+":"+value+ "\n")
                print("written succesfully")
        elif(c==2):
            value =input("Type here\n")
            with open ("Harry_food.txt", "a") as f:
                f.write(str([str(getdatetime())])+":"+value+"\n")
                print("written succesfully")
        else:
            print("try proper command")
    elif k==2:
        c=int(input("Enter 1 for excercise and 2 for diet:\n"))
        if c==1:
            value = input("Type here:\n")
            with open("Rohan_ex.txt","a") as f:
                f.write(str([str(getdatetime())])+":"+value+"\n")
                print("Written Succesfully")
        elif (c == 2):
            value = input("Type here\n")
            with open("Rohan_food.txt", "a") as f:
                f.write(str([str(getdatetime())]) + ":" + value + "\n")
                print("written succesfully")
        else:
            print("try proper command")
    elif k==3:
        c=int(input("Enter 1 for excercise and 2 for diet:\n"))
        if c==1:
            value = input("Type here:\n")
            with open("hammed_ex.txt","a") as f:
                f.write(str([str(getdatetime())])+":"+value+"\n")
                print("Written Succesfully")
        elif (c == 2):
            value = input("Type here\n")
            with open("hammed_food.txt", "a") as f:
                f.write(str([str(getdatetime())]) + ":" + value + "\n")
                print("written succesfully")
        else:
            print("try proper command")
    else:
        print("try proper command")

def  Retrive(k):
    if k==1:
        c=int(input("enter 1 for excercise, 2 for food:\n"))
        if c==1:
            with open("Harry_ex.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c==2:
            with open("Harry_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        else:
            print("try proper command")
    elif k==2:
        c=int(input("enter 1 for excercise, 2 for food:\n"))
        if c==1:
            with open("Rohan_ex.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c==2:
            with open("Rohan_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        else:
            print("try proper command")
    elif k==3:
        c=int(input("enter 1 for excercise, 2 for food:\n"))
        if c==1:
            with open("hammed_ex.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c==2:
            with open("hammed_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        else:
         print("try proper command")
    else:
        print("try proper command")

print("Health management System")
a=int(input("Enter 1 for log and 2 for retrive:\n"))
if a==1:
    b=int(input("enter 1 for harry, 2 for rohan, 3 for hammed:\n"))
    take(b)
elif a==2:
    b=int(input("enter 1 for harry, 2 for rohan , 3 for hammed:\n"))
    Retrive(b)
else:
    print("try proper command")

