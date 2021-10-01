import random

i = 1
points = 0
RunAgain = True

while RunAgain:

    rnum = random.randint(1, 100)
#    print(rnum)
    for i in range(1, 11):

        try:
            guess = int(input("Guess a number: "))

            if i != 10:
                pass
            else:
                print("*** Last chance ***")

            if guess == rnum:
                print("Lucky you!!! You found it after ", i - 1, " failed tries")
                points = 10 - i + 1
                print('You have won ', points,' points')
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
            if i!= 10:
               print("Please enter a number between 1 and 100")
            else:
                print("You lost!")
                break
                
    select: str = input("Wanna try again? (Y/N): " )
    if select == 'Y' or select == 'y':
        continue

    elif select == "N":
        print("Bye bye!!!!")
        break

    else:
        print("Goodbye!!")
        break



