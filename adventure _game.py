#import libraries we use
import random
import time 
from time import sleep

# functions of game
"""
function facilitate print and sleep cood
"""
def print_pause(text): 
    print(text)
    sleep(1)

"""
function which write the intro of game
to start playing
"""
def intro(print_pause):
    print_pause(f"Hello {char_name}")
    print_pause("There was a king lost his son")
    print_pause("Some fighters take king's son to pay him as slave")
    print_pause("Prince was has a strong body")
    print_pause("Prince resist the fighters in the way")
    print_pause("Prince run away to the forest")
    print_pause("Prince was so young ; so he dosn't get back to his country")
    print_pause("When the king realize the stollen of his son")
    print_pause("He commend soliders to find the prince")
    print_pause("But nothing changed \U0001F62A")
    print_pause("By the years")
    print_pause("Prince live in forest for all his life")
    print_pause("When he riding his horse and look out to eat his food")
    print_pause("He doesn't find his food \U0001F62C")
    print_pause("the food was stollen \U0001F603")
    print_pause("He was so hungry")
    print_pause("He find two stranges villages one GREEN and one GOLDEN")
    print_pause("Now you are the prince")
    print_pause("Which village you will get to")
    print_pause("REMEMBER you must collect 100 point in your score")
    print_pause("For Golden village press 1")
    print_pause("For Green village press 2")

"""
function of player score to know does he lose or win
and if he want to repeat or end game
"""
def score(char_score, char_name, char_dec):
    print_pause(f"your score is {char_score}")
    if char_score == 100:#<--win
        print_pause(f"GOOD job {char_name}")
        print_pause("you win \U0001F618")
        print_pause("For playing again press 1")
        print_pause("For not playing again prss 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1":#<--repeat game
            char_name = input("please enter your name: ").title()
            intro(print_pause)
        elif char_dec == "2":#<--end game
            print_pause("HOPE YOU PEACEFUL LIFE \U0001F618")
            print_pause("BYE")
    elif char_score <= 100:#<--lose
        print_pause(f"SORRY {char_name}")
        print_pause("you lose \U0001F62A")
        print_pause("For playing again press 1")
        print_pause("For not playing again prss 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1":#<--repeat game
            char_name = input("please enter your name: ").title()
            intro(print_pause)
        elif char_dec == "2":#<--end game
            print_pause("HOPE YOU PEACEFUL LIFE \U0001F618")
            print_pause("BYE")
    else:
        print_pause("YOU ARE BRILLIANT \U0001F607")
        print_pause("For playing again press 1")
        print_pause("For not playing again prss 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1":#<--repeat game
            char_name = input("please inter your name: ").title()
        elif char_dec == "2":#<--end game
            print_pause("HOPE YOU PEACEFUL LIFE \U0001F618")
            print_pause("BYE")

"""
function of scenario number one.
GAME contain --> scenario --> story --> story's result
--> win or lose
"""
def sc_1(char_dec, char_score = 0):
    while char_dec != "1" and char_dec != "2":
        char_dec = input("Enter: ")
    if char_dec == "1": #<--first choice from first scenario
        char_score += 50
        print_pause("WAIT")
        print_pause("YOU heard voice")
        print_pause("For keeping walk press 1")
        print_pause("for goto voice press 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1": #<--first choice in story
            print_pause("Find golden apple dealer,night was come")
            print_pause("For buy golden apple press 1")
            print_pause("for just stay this night 2")
            char_dec = input("Enter: ")
            while char_dec != "1" and char_dec != "2":
                char_dec = input("Enter: ")
            if char_dec == "1":#<--first choice in story's result
                char_score += 25
                print_pause("Now you eatin golden apple")
                print_pause("WHAT IS THAT \U0001F603")
                print_pause("Your memory refreshed from golden apple ")
                print_pause("You remmeber where is your country")
                print_pause("you find your dad \U0001F917")
                score(char_score, char_name, char_dec) #<-- win or lose
            elif char_dec == "2":#<--second choice in story's result
                print_pause("You stay this night in dealer's house")
                print_pause("WAIT...You find strange thing")
                print_pause("To explore what is press 1")
                print_pause("To just sleep press 2")
                char_dec = input("Enter: ")
                decision(char_dec)
                if char_dec == "1": #extra scenario for brilliants
                    char_score += 25
                    print_pause("WHAAT!!!")
                    print_pause("The dealer is one from figters ")
                    print_pause("To make him admit press 1")
                    print_pause("for just Sleep Now press 2")
                    char_dec = input("Enter: ")
                    while char_dec != "1" and char_dec != "2":
                        char_dec = input("Enter: ")
                    if char_dec == "1": #extra scenario for brilliants
                        char_score += 25
                        print_pause("You did it \n mission completed")
                        print_pause(f"Great {char_name}")
                        print_pause(f"Your score is {char_score}")
                        score(char_score, char_name, char_dec) #<-- win or lose
                    elif char_dec == "2": #extra scenario for brilliants
                        print_pause("You waked up")
                        print_pause("You ate golden apple from dealer")
                        print_pause("The dealer is one from figters")
                        print_pause("He put poison in the apple \n you died")
                        score(char_score, char_name, char_dec) #<-- win or lose
                elif char_dec == "2": #extra scenario for brilliants
                    print_pause("You waked up")
                    print_pause("You ate golden apple from dealer")
                    print_pause("The dealer is one from figters")
                    print_pause("He put poison in the apple \n You died")
                    score(char_score, char_name, char_dec) #<-- win or lose
        elif char_dec =="2": #<--second choice in story
            char_score += 25
            print_pause("Finally")
            print_pause("you find fighters who stollen you from the king")
            print_pause("For fight them press 1")
            print_pause("For ask them how to get food press 2")
            char_dec = input("Enter: ")
            while char_dec != "1" and char_dec != "2":
                char_dec = input("Enter: ")
            if char_dec == "1":
                char_score += 25
                print_pause("You beat them")
                print_pause("They told you where is your country")
                print_pause("You find your country")
                print_pause(f"GOOD job {char_name}")
                score(char_score, char_name, char_dec) #<-- win or lose
            elif char_dec == "2":
                print_pause("They told you keep going along the river")
                print_pause("And you will find a palm tree")
                print_pause("they put the poison in palm tree to kill you")
                print_pause("You died")
                score(char_score, char_name, char_dec)  #<-- win or lose 
    elif char_dec == "2": #first choice in story
        char_score += 50
        print_pause("There was beautiful gardens and rivers in this village")
        print_pause("For stay in it press 1")
        print_pause("For keep going press 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1": #first choice in story's result
            print_pause("you didn't  find any food in it")
            score(char_score, char_name, char_dec) #win or lose
        elif char_dec == "2": #second choice in story
            char_score += 50
            print_pause("You find fighters who stollen you")
            print_pause("And they admit where is your country")
            score(char_score, char_name, char_dec) #win or lose
       
"""
function of scenario number two.
GAME contain --> scenario --> story --> story's result
--> win or lose
"""
def sc_2(char_dec, char_score = 0):
    while char_dec != "1" and char_dec != "2":
        char_dec = input("Enter: ")
    if char_dec == "1": #first choice in second scenario
        char_score += 50
        print_pause("you find alot of people wear old golden clothes")
        print_pause("To ask them how to get food press 1")
        print_pause("To keep going to village press 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1": #first choice in story
            print_pause("They told you to keep going along to river")
            print_pause("to eat dates from palm tree to ate dates")
            print_pause("To go to palm tree press 1")
            print_pause("To eat from their food press 2")
            char_dec = input("Enter: ")
            while char_dec != "1" and char_dec != "2":
                char_dec = input("Enter: ")
            if char_dec == "1": #first choice in first story's result
                char_score += 25
                print_pause("Dates was enchanted")
                print_pause("You remember where is your country")
                score(char_score, char_name, char_dec) # win or lose
            elif char_dec == "2": #second choice in first story's result
                print_pause("They were the fighters who stollen you")
                print_pause("They put poison in your food \n You died")
                score(char_score, char_name, char_dec) # win or lose
        elif char_dec == "2": #second choice in story
            char_score += 25
            print_pause("You find golden apple dealer")
            print_pause("To buy from him press 1")
            print_pause("To ask him how to get food press 2")
            char_dec = input("Enter: ")
            while char_dec != "1" and char_dec != "2":
                char_dec = input("Enter: ")
            if char_dec == "1": #first choice in second story's result
                char_score += 25
                print_pause("You find some thing in apple")
                print_pause("...is that poison!!!!")
                print_pause("You beat dealer")
                print_pause("He admit where is your country")
                score(char_score, char_name, char_dec) # win or lose
            elif char_dec == "2": #second choice in second story's result
                print_pause("He told you to keep going along river")
                print_pause("You find palm tree to ear dates")
                print_pause("The guy you met was from fighters who stollen you")
                print_pause("He poison the palm tree \nYou died")
                score(char_score, char_name, char_dec) #win or lose
    elif char_dec == "2": #second choice in second scenario
        char_score += 50
        print_pause("You find a huge beautiful castle")
        print_pause("To get in it press 1")
        print_pause("To keep going press 2")
        char_dec = input("Enter: ")
        while char_dec != "1" and char_dec != "2":
            char_dec = input("Enter: ")
        if char_dec == "1":#first choice in story
            char_score += 50
            print_pause("OOH your dad was inside \U0001F618")
            score(char_score, char_name, char_dec) #win or lose
        elif char_dec == "2":#second choice in story
            print_pause("when you on way monster catch you \nYou died")
            score(char_score, char_name, char_dec) #win or lose
        
#playin game
char_name = input("please enter your name: ").title() #<--name of player

intro(print_pause) #<--intro of game

char_dec = input("Enter: ") #<--decision of player

random.choice([sc_1(char_dec),sc_2(char_dec)]) #<--#random 
