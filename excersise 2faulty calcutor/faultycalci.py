#Faulty  Calculater

#print("first number\n")
firstnumber =int(input())
#print("which operation")
operator=input()
#print("second number\n")
secondnumber =int(input())
if firstnumber==63 and secondnumber==43 and operator=='+':
   print("answer is",130)

elif firstnumber==220 and secondnumber==50 and operator=='-':
      print("answer is",210)

elif firstnumber==45 and secondnumber==5 and operator=='*':
      print("answer is",300)

elif firstnumber==500 and secondnumber==10 and operator=='/':
      print("answer is",20)
elif operator =='+':
         print("answer is")
         print(firstnumber+secondnumber)
elif operator=='-':
        print("answer is")
        print(firstnumber-secondnumber)
elif operator=='*':
        print("answer is")
        print(firstnumber*secondnumber)
elif operator=='/':
        print("answer is")
        print(firstnumber/secondnumber)
elif operator=='**':
        print("answer is")
        print(firstnumber**secondnumber)
else:
    print("syntex error")


