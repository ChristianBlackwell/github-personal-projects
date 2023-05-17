import random

tries = input("Would like to flip the bottle: Y / N? \n")

if tries == "N":
    print("Thank you, have a good day!")

while tries == "Y":
    bottle_flip = random.randint(1, 3)
    counter = 0

    if bottle_flip == 1:
        print("Aw, it didn't land!")
        counter += 1
        if counter > 0:

            tries = input("\nWould you like to flip again: Y / N? \n")
            if tries == "N":
                print("Thank you, have a good day!")

    if bottle_flip == 2:
        print("You landed the flip!")
        counter += 1
        if counter > 0:

            tries = input("\nWould you like to flip again: Y / N? \n")
            if tries == "N":
                print("Thank you, have a good day!")

    if bottle_flip == 3:
        print("You landed a cap flip!")
        counter += 1
        if counter > 0:

            tries = input("\nWould you like to flip again: Y / N? \n")
            if tries == "N":
                print("Thank you, have a good day!")
