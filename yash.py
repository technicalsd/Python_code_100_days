num = int(input("Enter the number to be reversed: ")) # Taking input from user
reverse = 0
while num > 0:
  remainder = num % 10     # Extracting the last digit of the number
  reverse = (reverse * 10) + remainder   # Adding the extracted digit to the reversed number
  num = num//10     # Removing the last digit from the number
print("The reversed number is:", reverse)   # Printing the reversed number

