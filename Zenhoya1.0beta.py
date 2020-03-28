#Zenhoya Virtual assistant
#Simple chatbot, Lisara Jeewandara
import time
import sys
import random
print("Hello and Welcome!\n")
print("I am Zenhoya, your virtual assistant. How can I help you?")
print("To start, you might as well introduce yourself to me!")
name = input("Hello! What's your name")
namecheck = str(input("So your name is " + str(name) + ". Is that correct?"))
if namecheck == "yes":
    age = int(input("How old are you, in years"))
else:
    while namecheck != "yes":
        name = input("What's your name")
        namecheck = str(input("So your name is " + str(name) + ". Is that correct?"))
        age = int(input("How old are you, in years?"))
print("Great! That's all I need for now!")
time.sleep(5)
print("So, why do I collect your name and age? It's to build up customized answers for you.")
print('''So your profile is:
Name: ''' + str(name) + '''
Age:  ''' + str(age))
while True:
    question = sys.stdin.readline()
    if question == "What's the weather like?\n":
        print("There is a 20% chance of rain and a 100% chance of coronavirus")
    elif question == "What's the time?\n":
        print(time.asctime())
    elif question == "Thanks\n":
        print("You're welcome!\n")
    elif question == "Hello\n":
        print("Hello to you too!")
    elif question == "Tell me a joke\n":
        if 5 < age < 21:
            jokelistyoung = ["Why do gorillas have big fingers?\nBig nostrils!", "What's the difference between a banana and an elephant?\nYou can't peel an elephant!", "What happened to the guy who sued over his missing luggage?\nHe lost his case."]
            print(random.choice(jokelistyoung))
        elif 21 < age < 59:
            dadjokes = ["How do you weigh a millennial?\nIn Instagrams.", " What kind of tree has a hand? A palm tree.", "DAD: I was just listening to the radio on my way in to town, apparently an actress just killed herself.\nMOM: Oh my! Who!?\nDAD: Uh, I can't remember... I think her name was Reese something?\nMOM: WITHERSPOON!!!!!???????\nDAD: No, it was with a knife..."]
            print(random.choice(dadjokes))
        else:
            print("Huuuuh???🤔")
    elif question == "Roll dice\n":
        print(random.randint(1, 6))
    elif question == "Pick a card\n":
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        cards = ["Ace",  "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "King", "Queen", "Jack"]
        print(random.choice(cards) + " of " + random.choice(suits))
    elif question == "version\n":
        print("Zenhoya Version 1.01 Preview Build")
    elif question == "be annoying\n":
        animals = ["Marmot", "Pig", "Baboon", "Fowl", "Chicken"]
        parts = ["Nose", "Mouth", "Butt", "Head"]
        characteristic = ["half-faced", "big-headed", "pigheaded", "stinky", "mentally retarded", "idiotic", "imbicelic"]
        print("Your " + random.choice(parts)  + " is like " + "a(n)" + characteristic + animals)
    elif question == "bye\n":
        print("See you later. I hope my assistance has greatly helped you")
        break
    elif question == "Shut up!\n":
        print("OK. Sorry if I disturbed you")
        break
    else:
        print("Huh?")


