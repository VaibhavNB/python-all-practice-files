n = 18
numberofguesses=1
print(" maxmium attempts are 9")
print("Guess the number:\n")

while(numberofguesses<=9):
    guessthenumber = int(input())
    if guessthenumber>n:
        print("Try lesser number")
    elif guessthenumber<n:
        print("try higer number")
    else:
      print("congratulations..........\n you are the winnner")
      print(numberofguesses,"number of attempts")
      break
    print(9-numberofguesses,"attempts left with you")
    numberofguesses=numberofguesses+1

if(numberofguesses>9):
    print("game over... you lose buddy")

# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if(number_of_guesses>9):
#     print("Game Over")