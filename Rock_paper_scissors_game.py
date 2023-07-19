import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



input1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if input1 == 0:
    print(rock)
elif input1 == 1:
    print(paper)
else:
    print(scissors)


input2 = random.randint(0,2)
print("Computer choose:")

if input2 == 0:
    print(rock)
elif input2 == 1:
    print(paper)
else:
    print(scissors)

end  = str(input1)+str(input2)


if (end == "00" or end == "11" or end == "22"):
    print("It's Draw")
if (end == "02" or end == "10" or end == "21"):
    print("You Won!")
if (end == "01" or end == "12" or end == "20"):
    print("You lose")



