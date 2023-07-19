#Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))

perc = int(input("What precentage tip would you like to give? 10, 12, or 15? "))

nopeople = float(input("How many people to split the bill? "))
print("Each personshould pay: $",round((bill+perc*0.01*bill)/nopeople,2))