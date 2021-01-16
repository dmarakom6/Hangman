import random
import Info
open('wordsList.py', 'r')


 ##welcoming
print("Hello.\nWelcome to hangman!")



##menu
def menu():
    ##menu options
    print("Select one of the three options by typing 1,2 or 3:\n")
    print("1.Play")
    print("2.How to Play")
    print("3.Quit")
    while True:
        selection = int((input("Enter a number (1,2,3): ")))
        if selection == 3:
            print("OK. quitting...")
            exit();
        elif selection == 2:
            print("Loading game info and rules...")
            print()
            infomenu()
        elif selection == 4:
            easteregg()
        elif selection == 1:
            get_word()
            break
        elif selection not in 1 or 2 or 3 or 4:
            print("That input was not valid!")




def infomenu():
    nums2 = ["1", "2", "3", "4", "5", "6", "7"]
    print("This is the game information menu.\nChoose a number, or go back.")
    print("1.Game info")
    print("2.Game rules")
    print("3.Game History")
    print("4.Game strategy")
    print("5.Contact info about the maker")
    print("6.Go back to menu")
    print("7.Quit")
    while True:
        infoselection = int(input())
        if infoselection == 1:
            print(info)
        elif infoselection == 2:
            print(rules)
        elif infoselection == 3:
            print(history)
        elif infoselection == 4:
            print(strategy)
        elif infoselection == 5:
            print(maker)
        elif infoselection == 6:
            return menu
        elif infoselection == 7:
            print("OK. quitting...")
            exit();
        elif infoselection not in nums2 or len(infoselection) > 1:
            print("That input was not valid!")
            continue

def easteregg():
    print("Congrats!\nYou've found an easter egg!")
    prize = input("press the Enter key to view the word list!\n")
    import wordsList

def get_word():
    openfile = open("words.txt", "r")
    with open('words.txt') as f:
        mylist = f.read().splitlines()
    import random
    return random.choice(mylist)
    game_round()


def game_round():
    word = get_word()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters_guessed = []
    tries = 6
    guessed = False
    print("The word contains", len(word), "letters")
    display = print(len(word) * "_")
    while guessed == False and tries > 0:
        print("You have", tries, "Guesses left.")
        guess = input("Enter one letter or the full word:\n").lower()
        if len(guess) == 1:
            if guess not in alphabet:
                print("You have not entered a letter.")
            elif guess in letters_guessed:
                print("You have already guessed that letter before.")
            elif guess not in word:
                print(guess, "?", " I don't think so...")
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print("That's right!")
                letters_guessed.append(guess)
            else:
                print("That didn't work.")
        elif len(guess) == len(word):
            if guess == word:
                print("Good Job!\nYou've found it!")
                guessed = True
            else:
                print("Nope. That's not the word")
                tries -= 1
                guessed = False
        else:
            print("That's not the right length.")

        status = ""
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += "_"
            print(status)
        if status == word:
            print("Congrats!\nYou've found it!")
            guessed = True
        elif tries == 0:
            print("You've ran out of guesses, and still haven't found the word!\nYou lost!")
            print(word)
def play_again():
    repeat = input("Would you like to play again?\n[Y/N]: ").lower()
    yes = ["yes", "y", "yep",]
    no = ["no", "n", "nope"]
    answers = yes + no
    while True:
        if repeat not in answers:
            print("That input was not valid!")
            return play_again();
        elif repeat in no:
            print("Fine. See you later!")
            import time
            time.sleep(1)
            exit();
            break
        elif repeat in yes:
            print("OK. Starting round in:")
            import time
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1!")
            time.sleep(0.2)
            clear()
            game_round()
            play_again()
            break

       

def clear():
    import sys
    cls = "\n"
    print(cls * 100)






##run
menu()
game_round()
play_again()
