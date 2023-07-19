# 🚨 Don't change the code below 👇
sum = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    # 🚨 Don't change the code above 👆
    sum = sum + student_heights[n]

# Write your code below this row 👇
Avg = sum / len(student_heights)
print(round(Avg))
