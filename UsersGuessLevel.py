import random


class GameLevel:
    def game_level_is_easy(self):
        guessed_number_by_computer = random.randint(1, 10)
        print("You have 6 guesses")
        for i in range(6):
            user_guess = int(input("Guess a number between 1-10: "))
            if user_guess == guessed_number_by_computer:
                print("Congratulations, you got it right")
            else:
                i += 1
                y = 6 - i
                if y != 0:
                    print("That was wrong, try again")
                    print(f"You have {y} guess(es)")
                else:
                    print("Game Over!")

    def game_level_is_medium(self):
        guessed_number_by_computer = random.randint(1, 20)
        print("You have 4 guesses")
        for i in range(4):
            user_guess = int(input("Guess a number between 1-20: "))
            if user_guess == guessed_number_by_computer:
                print("Congratulations, you got it right")
            else:
                i += 1
                y = 4 - i
                if y != 0:
                    print("That was wrong, try again")
                    print(f"You have {y} guess(es)")
                else:
                    print("Game Over!")

    def game_level_is_hard(self):
        guessed_number_by_computer = random.randint(1, 50)
        print("You have 3 guesses")
        for i in range(3):
            user_guess = int(input("Guess a number between 1-50: "))
            if user_guess == guessed_number_by_computer:
                print("Congratulations, you got it right")
            else:
                i += 1
                y = 3 - i
                if y != 0:
                    print("That was wrong, try again")
                    print(f"You have {y} guess(es)")
                else:
                    print("Game Over!")
