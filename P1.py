import random

def generate_random_number():
    digits = list(range(1, 10))  # 1-9 (first digit can't be 0)
    random.shuffle(digits)  # Shuffle digits
    number = ''.join(map(str, digits[:3]))  # Pick 3 unique digits
    return (number)

def check_bulls_and_cows(random_number,user_guess):
    bulls =sum(1 for i in range(3) if user_guess[i]==random_number[i])#digits matched and position matched
    cows=sum(1 for i in range(3) if user_guess[i] in random_number and user_guess[i]!=random_number[i])# digit matched and position not matched
    return cows,bulls

def main_game():
    random_number=generate_random_number()
    attemps=8
    Name=input("Enter your name:")
    print("Hi",Name,", Lets start the Game")

    for i in range(8):
        user_guess=input(f"Attempt {9-attemps}/8: enter your guess: ")
        if not user_guess.isdigit() or len(user_guess) != 3 or len(set(user_guess)) !=3:
            print("Invaild input! enter a 3 digit number with unique digits.")
            continue
        cows,bulls=check_bulls_and_cows(random_number,user_guess)
        print(f"Bulls:{bulls}, Cows:{cows}")
        if bulls==3:
            print(f"You Won! the number was{random_number}.")
            return
        attemps-=1
    print(f"You lost the game The correct number is {random_number}.")

main_game()
