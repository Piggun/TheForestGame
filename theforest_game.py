import time
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import random

weapons = ["knife", "sword", "hammer", "fork", "spear", "wrench"]
animals = ["jaguar", "tiger", "lion", "gorilla", "hyena"]


def print_pause(text, num):
    print(text)
    time.sleep(num)


def play_game():
    random_weapon = random.choice(weapons)
    random_animal = random.choice(animals)
    inventory = []
    while True:
        intro()
        while True:
            choice = input("(Enter 1 or 2.) : ")
            if choice == "1":
                first_choice(inventory, random_weapon, random_animal)
                break
            if choice == "2":
                second_choice(inventory, random_weapon, random_animal)
                break
        break


def play_again():
    response = input("Would you like to play again? (y/n)")
    if response == "y":
        print()
        play_game()
    if response == "n":
        print("\nThanks for playing!\n")
        sys.exit()
    else:
        print("Please enter 'y' or 'n'. \n\n")
        play_again()


def intro():
    print_pause(Fore.BLACK + Back.RED + "    THE FOREST    "
                + Style.RESET_ALL + "\n", 2)
    print_pause("You find yourself in a flourishing forest, "
                "feeling quite confused.", 2)
    print_pause("You've got two choices: ", 1)
    print_pause("1. Start walking hoping to find a way out.", 1)
    print_pause("2. Look for a high ground.", 1)


def lost_game():
    print_pause(Fore.RED + "\nThe flourishing forest watches you die. \n", 1)
    print_pause("You loose.", 1)
    print_pause("GAME OVER \n" + Style.RESET_ALL, 1)
    play_again()


def won_game():
    print(Fore.YELLOW + "\nCongratulanions!")
    print_pause("You win!", 1)
    print_pause("GAME OVER \n" + Style.RESET_ALL, 1)
    play_again()


def first_choice(inventory, random_weapon, random_animal):
    print_pause("\nYou decide to venture yourself in "
                "the overwhelming forest wihout a plan,", 2)
    print_pause("After a few minutes of walk you start to feel anxious,", 2)
    print_pause("Your breath gets louder,", 1)
    print_pause("Heavier,", 1)
    print_pause("Your palms start sweating,", 1)
    print_pause("Shaking,", 1)
    print_pause("Your heart's goin' off like crazy:", 1)
    print_pause(Fore.RED + "<bo boom>", 1)
    print_pause("<Bo Boom>", 1)
    print_pause("<BO BOOM>" + Style.RESET_ALL, 1)
    print_pause("You have no idea which way to go:", 1)
    print_pause("1. Start screaming for help.", 1)
    print_pause("2. Get a grip and start walking "
                "towards a fixed direction.", 1)
    while True:
        choice1 = input("(Enter 1 or 2.) : ")
        if choice1 == "1":
            print_pause(Fore.BLUE + "\n'Help!'", 1)
            print_pause("'HELP!! PLEASE HELP ME!!'" + Style.RESET_ALL, 3)
            print_pause("Nobody hears your call,", 1)
            print_pause("You let your emotions take over you,", 2)
            print_pause("You lay down flat on the ground,", 2)
            print_pause("Thinking what a useless piece of human "
                        "wihout any kind of survival ability you are.", 3)
            lost_game()
            break
        elif choice1 == "2":
            print_pause("\nYou get yourself together,", 1)
            second_choice(inventory, random_weapon, random_animal)
            break


def second_choice(inventory, random_weapon, random_animal):
    print_pause("\nYou spot a radio tower a few miles away, "
                "it's on top of a mountain, "
                "you decide to head towards it. ", 2)
    print_pause(Fore.GREEN + "<Pam...Pam>", 1)
    print_pause("<Pam...Pam>", 1)
    print_pause("<Pam...Pam>" + Style.RESET_ALL, 1)
    print_pause("As you walk through the forest you notice "
                "a glint underneath a branch.", 2)
    print_pause("You get closer to have a better look..", 1)
    print_pause(f"It's a {random_weapon} :", 1)
    print_pause("1. Pick it up", 1)
    print_pause("2. Ignore it and keep walking", 1)
    while True:
        choice2 = input("(Enter 1 o 2.) : ")
        if choice2 == "1":
            print_pause(f"\nYou pick up the {random_weapon}"
                        " and get back to your path.", 1)
            inventory.append(random_weapon)
            break
        if choice2 == "2":
            print_pause(f"\nYou ignore the {random_weapon} "
                        "and get back on your path.", 1)
            break
    print_pause(Fore.GREEN + "<Pam...Pam>", 1)
    print_pause("<Pam...Pam>", 1)
    print_pause("<Pam...Pam>" + Style.RESET_ALL, 1)
    print_pause("While getting closer to the mountain you hear "
                "an unexcpected noise behind your back..", 2)
    print_pause(Fore.YELLOW + "\n<CRACK>\n" + Style.RESET_ALL, 2)
    print_pause("You turn around,", 1)
    print_pause(f"A {random_animal} jumps out of a bush and attacks you.", 1)
    print_pause("What do you do? :", 1)
    print_pause("1. Attack.", 1)
    print_pause("2. Run. ", 1)
    while True:
        choice3 = input("(Enter 1 or 2.) : ")
        if choice3 == "1":
            if random_weapon in inventory:
                print_pause(f"\nThe ferocious {random_animal} "
                            "charges at you, ", 2)
                print_pause(f"You rapidly unsheathe "
                            f"your {random_weapon}, ", 1)
                print_pause("Get a good grip and stick it "
                            "right between his eyes.", 2)
                print_pause(Fore.RED + "'uuuh..'", 1)
                print_pause("'AAAAAHHH!!!!!'" + Style.RESET_ALL, 3)
                print_pause("After a loud groan "
                            "the fierce beast falls to the ground.", 2)
                break
            else:
                print_pause(f"\nThe ferocious {random_animal} "
                            "charges at you,", 1)
                print_pause("You try to fight back with all your strenght "
                            "but he's too strong and he shreds you alive.", 2)
                print_pause(f"A {random_weapon} would have been handy.", 2)
                lost_game()
                break
        elif choice3 == "2":
            print_pause("\nYou start running :", 1)
            print_pause(Fore.GREEN + "<Pa Pam>", 0.5)
            print_pause(Fore.GREEN + "<Pa Pam>", 0.5)
            print_pause(Fore.GREEN + "<Pa Pam>", 0.5)
            print_pause(Fore.GREEN + "<Pa Pam>" + Style.RESET_ALL, 2)
            print_pause(f"Inexplicably you manage to overcome "
                        f"the {random_animal} and get back to safety.", 3)
            break
    print_pause("\nA few hours later you finally get "
                "to the base of the mountain.", 3)
    print_pause("You climb it until you reach the peak.", 2)
    print_pause("By looking at the view you find out "
                "to be in a deserted island.", 3)
    print_pause("Next to the radio tower there's "
                "a small shack, you head inside.", 3)
    print_pause("The shack is filled with radio equipment "
                "that's still magically working.", 3)
    print_pause("What do you do? :", 1)
    print_pause("1. Use the radio.", 1)
    print_pause("2. Don't use the radio.", 1)
    while True:
        choice4 = input("(Enter 1 or 2.) : ")
        if choice4 == "1":
            print_pause("\nYou use the radio to call for help.", 2)
            print_pause("A fishing boat near the island gets your call "
                        "and comes to your rescue.", 2)
            print_pause("You manage to get out of the island alive.", 2)
            won_game()
            break
        elif choice4 == "2":
            print_pause("\nYou despise technology and "
                        "you decide to not use the radio.", 2)
            print_pause("There's nothing else left to do.", 2)
            print_pause("You jump down the mountain,", 2)
            print_pause(Fore.RED + "\n <SPLAT> \n" + Style.RESET_ALL, 2)
            print_pause("Your head splashes on a pointy rock.", 2)
            lost_game()
            sys.exit()
            break


# main
play_game()
