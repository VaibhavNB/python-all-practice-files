
n=int(input())
list1=list(map(int,input().split(" ")))
k=max(list1)
for i in range(n):
     if max(list1)==k:
          list1.remove(max(list1))
list1.sort(reverse=True)
print(list1[0])


# print(a)

# # max(arr)
# n = int(input())
# arr = list(map(int, input().split(" ")))
# k = max(arr)
# for i in range(0, n):
#      if max(arr) == k:
#           arr.remove(max(arr))
# arr.sort(reverse=True)
# print(arr[0])