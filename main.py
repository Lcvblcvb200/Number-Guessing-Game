import random

print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100. \n You have 5 chances to guess the correct number.")
print("Please select the difficulty level: \n 1. Easy (10 chances) \n 2. Medium (5 chances) \n 3. Hard (3 chances)")
dif = int(input("Enter your choice: "))

if dif == 1:
    print("You've choosen the Easy mode (10 chances) \n Let's start the game!")
    chances = 10
elif dif == 2:
    print("You've choosen the Medium mode (5 chances) \n Let's start the game!")
    chances = 5
elif dif == 3:
    print("You've choosen the Hard mode (3 chances) \n Let's start the game!")
    chances = 3

numero = random.randint(1, 100)
tentativas = 0
for i in range(chances):
    escolha = int(input("Enter your guess: "))
    if escolha > numero:
        print(f"Incorrect! The number is less than {escolha}")
        tentativas += 1
    elif escolha < numero:
        print(f"Incorrect! The number is greater than {escolha}")
        tentativas += 1
    else:
        print(f"Congratulations! You guessed the correct number in {tentativas} attempts.")
    if tentativas == chances:
        print(f"Your guesses are over! \n The number was: {numero}")
        