# Calculator program for faulty calculation
print("This is your calculator for exam")
print("For sum select +, for multiply select *, for division select /,for subtraction select-, for power select **")
num1=int(input("Enter your first no: "))
num2=int(input("Enter your second no: "))
operator=input("select your operation: ")
if operator=="+" and num1==56 and num2==9: #Faulty output
    print("Your output is:",77)
elif operator=="*" and num1==45 and num2==3: #Faulty output
    print("Your output is:",55)
elif operator=="/" and num1==56 and num2==6: #Faulty output
    print("Your output is:",4)
elif operator=="+":
    print("Your output is:",num1+num2)
elif operator=="-":
    print("Your output is:",num1-num2)
elif operator=="/":
    print("Your output is:",num1/num2)
elif operator=="*":
    print("Your output is:",num1*num2)
elif operator=="**":
    print("Your output is:",num1**num2)