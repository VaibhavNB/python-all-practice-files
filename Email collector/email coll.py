#take str input and extract the email from the given str
# import re
# def vaibhav():
#     v=int(input())
#     b=int(input())
#     sum=v+b+b+b+b+v+v
#     print(sum)
#
# # s=str(input("Enter the str:\n"))
# #
# # email= re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",s)
# # print(email)
# # vaibhav()
# vaibhav()

import math
T=int(input())
for i in range (T):
    (a,b)=map(int ,input().split(" "))
    ans=a+b
    with open("file.txt","ap") as f:
        f.write(ans)










