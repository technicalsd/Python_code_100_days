logo ='''
   _____                                _     _                                            _                   
  / ____|                              | |   | |                                          | |                  
 | |  __   _   _    ___   ___   ___    | |_  | |__     ___     _ __    _   _   _ __ ___   | |__     ___   _ __ 
 | | |_ | | | | |  / _ \ / __| / __|   | __| | '_ \   / _ \   | '_ \  | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |__| | | |_| | |  __/ \__ \ \__ \   | |_  | | | | |  __/   | | | | | |_| | | | | | | | | |_) | |  __/ | |   
  \_____|  \__,_|  \___| |___/ |___/    \__| |_| |_|  \___|   |_| |_|  \__,_| |_| |_| |_| |_.__/   \___| |_|   
'''


#________Created by self _____----> Saurabh D

print(logo)
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num =  random.randint(1,100)
# print(f"Psst, the correct answer is {num}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
if difficulty == 'easy':
    attempt = 10
else:
    attempt = 5
end_game = 0
while attempt>0 and end_game==0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempt -= 1

    if difficulty == "easy":
        if guess == num:
            print(f"You got it! The answer was {num}")
            end_game = 1

        if guess > num:
            print(f"Too high")
        elif guess< num:
            print(f"Too low")

    if difficulty == "hard":
        if guess == num:
            print(f"You got it! The answer was {num}")
            end_game = 1
        if guess > num:
            print(f"Too high")
        elif guess<num:
            print(f"Too low")


            
if attempt == 0:
    print("You have run out of guesses, you lose.")
    print(f"Correct number to guess was {num}")
