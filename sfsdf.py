f = open("my_file.txt","a+")

x = int(input("Enter number"))


f.write(str(x))

sum = 0

c = len(str(x))-1

while x!=0:
    d = x%10
    sum = sum+d*(10**c)
    c = c-1
    x = x//10

f.write(str(sum))

w = f.r()

print(w)

