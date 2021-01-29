# pattern printing
print("::Star pattern printing::")
rows=int(input("enter number of rows: \n"))
print("enter 1 or 0")
bool_val=input("1 for True and 0 for False: \n")
if bool_val=="1":
    for i in range(0,rows+1):
        print("*"*int(i))
elif bool_val=="0":
    for i in range(rows,0,-1):
        print("*"*int(i))