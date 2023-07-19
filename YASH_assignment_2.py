# SUM OF FIRST n NATURAL NUMBERS

# num=int(input("Enter the number upto which the sum has to be found:\n"))
#
# if num < 0 :
#      print("Enter a positive number")
# else :
#     sum = 0
#     # use while loop to iterate untill zero
#     while(num >0):
#        sum += num
#        num -= 1
#     print("The sum is", sum)

# SUM OF FIRST 100 NATURAL NUMBERS

# x= int(input("Enter the number upto which the sum has to be found :\n"))
#
# if x < 0 :
#     print("Enter a positive number")
#
# else :
#     sum = 0
#     for y in range(0, x+1):
#         sum+=y
#     print(sum)

# AVERAGE OF AGE OF 10 PLAYERS :

# n = int(input("Enter the number of players whose age needs to be considered to get average:\n"))
# sum = 0
# for x in range(0, n):
#     age = int(input(f"Enter the age of {x+1} player"))
#     sum += age
# avg=sum//n
# print(f"Average of ages of all the players is {avg} years")


# SUM OF n ODD & EVEN NUMBERS :
# num = int(input("Enter the no. upto which sum has to be found:\n"))
# se=0
# so=0
# for x in range(0,num+1):
#     if x % 2==0:
#         se+=x
#     else:
#         so+=x
#
# print("Sum of even numbers is", se)
# print("Sum of odd numbers is", so)


# TO FIND 1st n ODD AND EVEN NUMBERS :
'''
num = int(input("Enter the number upto which odd or even numbers has to be found\n"))
comp1=0
comp2=0
for x in range(0, num+1):
    if x % 2 == 0 :
        comp1+=1
        print(x, end=",")
print("these are the found even numbers")

for y in range(0, num+1):
    if y % 2 == 1:
        comp2+=1
        print(y, end=",")
print("these are the found odd numbers")

total_comparison = comp1 + comp2

print(f"The total number of final comparisons is {total_comparison} .")
'''


# TO FIND THE FACTORIAL OF N NUMBER:

# num = int(input("Enter the number whose factorial has to be found :\n"))
# prod = 1
#
# while (num > 0) :
#     prod *= num
#     num -= 1
# print(f"The factorial of entered number is {prod}. ")

# num = int(input("Enter the number whose factorial has to be found :\n"))
# prod = 1
#
# for x in range(1, num+1):
#     prod *= x
# print(f"The factorial of entered number is {prod}.")


# DETERMINING PRIME NUMBER:
# num = int(input("Enter the number :\n"))
# if num > 1:
#     for x in range(2, int(num/2)+1):
#         if num % x == 0:
#             print(f"{num} is not a prime number")
#             break
#         else:
#             print(f"{num} is a prime number")
#             break
# else:
#     print(f"{num} is not a prime number")


# GENERATE FIRST N NUMBERS OF FIBONACCI SERIES:
# num = int(input("Enter the no. of terms of fibonacci series required :\n"))
# num1 = 0
# num2 = 1
# next_number = 0
# count = 1
# while (count <= num):
#     count += 1
#     num1 = num2
#     num2 = next_number
#     next_number = num1 + num2
#     print(next_number, end= " ")


# DECIMAL TO BINARY CONVERSION :

# num = int(input("Enter the Decimal number:\n"))
#
# binary_number = bin(num)
#
# print(f"Binary number of {num} is {binary_number}.")

# 2. WITHOUT USING BIN INBUILT FUNCTION :

# num = int(input("Enter  a decimal number:\n"))
#
# l = []
# while (num>=1):
#     x = num % 2
#     l.append(x)
#     num //= 2
#
# l.reverse()
#
# for x in l:
#     print(x,end="")


n = int(input())

ans = 0

while(n > 0):

    last = n % 2
    ans += ans*10 + last
    n //= 2

print(ans)








