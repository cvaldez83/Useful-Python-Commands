import random
import time

def displayIntro():
    print("You are in a land full of dragons.")
    time.sleep(2)
    print('''In front of you, you see two caves.
    In one cave, the dragon is friendly and will share his treasure with you.
    The other dragon is greedy and hungry, and will eat you on site.''', '\n')

def chooseCave():
    cave = " "
    while cave != '1' and cave != '2':
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out and...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print("gives you his treasure!")
    else:
        print("Gobbles you up!")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    caveNumber = chooseCave()

    checkCave((caveNumber))
    print("Do you wanna play again?")
    playAgain = input()
