# ASSIGNMENT 5

#Q.1

# a = []
#
# n = int(input("Enter number of element:-"))
#
# for x in range(0,n):
#     y = int((input("Enter Element:-")))
#     a.append(y)
# print("Original List:-",a)
# for i in range(0,n//2):
#     temp = a[i]
#     a[i] = a[n-i-1]
#     a[n-i-1] = temp
#
# print("Reversed list:- ",a)

#Q2

listt = []

n = int(input("Enter number of element:-"))

for x in range(0,n):
    y = int((input("Enter Element:-")))
    listt.append(y)

# Linear Search
key = int(input("Enter the number:-"))

# is_true = False
# for x in listt:
#     if key == x:
#         is_true = True
#         break
#     else:
#         continue
#
# if is_true == True:
#     print("Succesful Search")
# else:
#     print("Unsuccesful Search")

#Binary Search

listt.sort()

print(listt)
low = 0
high = n- 1

while low <= high:
    mid = (low + high)//2
    if listt[mid] == key:
        print("Succesful search at ",mid)
        break
    elif listt[mid]>key:
        high = mid - 1
    else:
        low = mid+1
else:
    print("Unsuccesful Search")










