# Random number game. Asks from user to guess a number between 1 and 100
# that was generated from random function.
#

import random

points = 0
RunAgain = True
score = []

while RunAgain:

    rnum = random.randint(1, 100)
#    print(rnum)
    for i in range(1, 11):

        try:
            guess = input("Guess a number (or exit to leave game): ")
            if guess == 'exit':
                print("Thank you for playing, hope to see you again!")
                break
            else:
                guess = int(guess)

                if i != 10:
                    pass
                else:
                    print("*** Last chance ***")

                if guess == rnum:
                    print("Lucky you!!! You found it after ", i - 1, " failed tries")
                    points = 10 - i + 1
                    score.append(points)
                    print("You have won ", points, " points")
                    break

                elif guess < rnum:
                    if i == 10:
                        print("Sorry mate, you lost")
                        break
                    else:
                        print("Aim higher...")

                elif guess > rnum:
                    if i == 10:
                        print("Sorry mate, you lost")
                        break
                    else:
                        print("Aim lower...")

        except:
            if i != 10:
                print("Please enter a number between 1 and 100")
            else:
                print("You lost!")
                break

    if guess == "exit":
        if len(score) == 0:
            break
        else:
            print("Your score during each game was: ", score)
            break
    else:
        select: str = input("Wanna try again? (Y/N): ")
        if select == 'Y' or select == 'y':
            continue
        elif select == "N":
            print("Bye bye!!!!")
            print("Your score during each game was: ", score)
            break
        else:
            print("Goodbye!!")
            print("Your score during each game was: ", score)
            break
