#Who are your friends?
from time import sleep
from random import *
print("Type 'start()' to start!")
def debug():
    print("This Doesnt Exist Yet. Hold ya Horses!")
def start():
    friend1 = input("Pick a friend: ")
    friend2 = input("Pick another friend: ")
    friend3 = input("Pick a final friend: ")

    friends = [friend1, friend2, friend3,]

    print("Your friends are: ", friends[0],",", friends[1],"and", friends[2])


    print("Im doubtful!")
    sleep(1)
    print("Why did you include", friends[2], "i've changed it for you dont worry!")
    sleep(1)
    number = randint(1,3)
    if number == 1:
        friends[2] = "Fortnite Ninja"
    elif number == 2:
        friends[2] = "Blue Hair Funny Man"
    elif number == 3 and friends[0].lower() != "thom" and friends[1].lower() != "thom" and friends[2].lower() != "thom":
        friends[2] = "Thom"
    elif number == 3:
        friends[2] = "Pronoun Man"
    else:
        pass
    print("Your new friend is", friends[2])
    if number == 3 and friends[2].lower() == "pronoun man":
        pronouns = input("Oh by the way. What are your pronouns? ")
        if pronouns.lower() == "it":
            gender = "Thing"
        elif pronouns.lower() == "him":
            gender = "Male"
        elif pronouns.lower() == "she":
            gender == "Female"
        else:
            gender = "unknown"
        print("Ok your pronouns are", pronouns)
        if gender.lower() == "thing" or gender.lower() == "male" or gender.lower() == "female":
            print("and you're a", gender)
        elif gender.lower() == "unknown":
            pass

def Keiran():
    print("So guys we did it. A code that askes Kerian what his pronouns are!")

#So guys we did it. A code that askes Kerian what his pronouns are!
