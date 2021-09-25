import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys

player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start",
    "health" : 3
}

# Check player's health
def checkHealth():
    if player["health"] > 0:
        print ("Health - 1")
        return player["health"]
    else:
        printGraphic("death")
        print ("You die! Game over!")
        print ("________________________________________________________")
        exit()

def rollDice(difficulty):
    # roll a dice for the first time
    raw_input("press [enter] to roll the dice for the first time >")
    result1 = random.randint(1,6)
    print ("You roll a: " + str(result1))
    # the second time
    raw_input("press [enter] to roll the dice for the second time >")
    result2 = random.randint(1,6)
    print ("You roll a: " + str(result2))
    total = result1 + result2
    print ("_____________________________________________________________")
    print ("Add up to " + str(total))

    if (total <= difficulty):
        player["health"] -= 1
        checkHealth()
        for x in range(player["health"]):
            printGraphic("health")
        print ("")
        print ("trying again....")
        rollDice(difficulty)
    else:
        return # back to flightSlime

def happyEnding():
    print (player["name"] + ", my hero!")
    print ("You have beaten down all evil creatures in this dungeon!")
    raw_input("press [enter] >")
    print ("You find a treasure chest. It's all yours!")
    printGraphic("chest")
    exit()

def fightGhost():
    print ("Let's roll a dice twice!")
    print ("If the numbers add up to larger than 9, you can beat the Ghost!")
    difficulty = 9
    rollDice(difficulty)
    print ("You beat the Ghostn!")
    print ("________________________________________________________")
    raw_input("press [enter] >")
    happyEnding()

def meetGhost():
    print ("Walking and walking...")
    raw_input("press [enter] >")
    print ("A shadow flits in front of you!")
    raw_input("press [enter] >")
    print ("Who's there?")
    raw_input("press [enter] >")
    print ("You saw a ghost floating in the air")
    printGraphic("ghost")
    raw_input("press [enter] >")
    print ("Do you want to fight or run away?")
    pcmd = raw_input("please choose [fight] or [run] >")

    if (pcmd == "fight"):
        print ("Let's fight!")
        raw_input("press [enter] >")
        fightGhost()
    elif (pcmd == "run"):
        print ("You turn around and run as fast as you can.")
        print ("You stepped on a trap and die...")
        printGraphic("death")
        print ("Game Over!")
        print ("________________________________________________________")
        return
    else:
        print ("I don't understand.")
        meetGhost()

def fightLizard():
    print ("Let's roll a dice twice!")
    print ("If the numbers add up to larger than 6, you can beat the Lizard Man!")
    difficulty = 6
    rollDice(difficulty)
    print ("You beat the Lizard Man!")
    print ("________________________________________________________")
    raw_input("press [enter] >")
    meetGhost()

def meetLizard():
    print ("Walking and walking...")
    raw_input("press [enter] >")
    print ("What's the giant creature standing in the shadow?")
    raw_input("press [enter] >")
    print ("It's a Lizard Man!")
    printGraphic("lizard")
    raw_input("press [enter] >")
    print ("Do you want to fight or run away?")
    pcmd = raw_input("please choose [fight] or [run] >")

    if (pcmd == "fight"):
        print ("Let's fight!")
        raw_input("press [enter] >")
        fightLizard()
    elif (pcmd == "run"):
        print ("You turn around and run as fast as you can.")
        print ("You stepped on a trap and die...")
        printGraphic("death")
        print ("Game Over!")
        print ("________________________________________________________")
        return
    else:
        print ("I don't understand.")
        meetLizard()

def fightSlime():
    print ("Let's roll a dice twice!")
    print ("If the numbers add up to larger than 4, you can beat the Slime!")
    difficulty = 4
    rollDice(difficulty)
    print ("You beat the Slime!")
    print ("________________________________________________________")
    raw_input("press [enter] >")
    if player["location"] == "left":
        meetLizard()
    # if player chose the right door
    else:
        print ("Walking and walking...")
        raw_input("press [enter] >")
        print ("Oops! It seems to be an dead end!")
        raw_input("press [enter] >")
        print ("Let's go back and try the other door.")
        player["location"] == "entry"
        dungeonEntry()

def meetSlime():
    print ("Walking and walking...")
    raw_input("press [enter] >")
    print ("What's the green light over there?")
    raw_input("press [enter] >")
    print ("You saw a glowing Slime that blocks your way!")
    printGraphic("slime")
    raw_input("press [enter] >")
    print ("Do you want to fight or run away?")
    pcmd = raw_input("please choose [fight] or [run] >")

    if (pcmd == "fight"):
        print ("Let's fight!")
        raw_input("press [enter] >")
        fightSlime()
    elif (pcmd == "run"):
        print ("You turn around and run as fast as you can.")
        print ("You stepped on a trap and die...")
        printGraphic("death")
        print ("Game Over!")
        print ("________________________________________________________")
        return
    else:
        print ("I don't understand.")
        meetSlime()


def dungeonEntry():
    print ("After walking in the dark for a while, you saw light in the distance.")
    raw_input("press [enter] >")
    print ("As you approach the light, you saw two giant wooden doors in front of you.")
    print ("Which way to go?")
    pcmd = raw_input("please choose [left] or [right] >")

    if (pcmd == "left"):
        print ("You open the left door and walk into the darkness...")
        raw_input("press [enter] >")
        player["location"] = "left"
        meetSlime()
    elif (pcmd == "right"):
        print ("You open the right door and walk into the darkness...")
        raw_input("press [enter] >")
        player["location"] = "right"
        meetSlime()
    else:
        print ("I don't understand.")
        dungeonEntry()


def introStory():
    # let's introduce them to our world
    print ("Welcome, my warrior!")
    pcmd = raw_input("press [enter] >")
    print ("May I know your name?")
    player["name"] = raw_input("Please enter your name >")

    # intro story
    print ("Nice to meet you, " + player["name"] + "!")
    raw_input("press [enter] >")
    print ("Before you enter the dungeon, I want to warn you that...")
    raw_input("press [enter] >")
    print ("Thousands people have stepped into the dungeon, but no one have gotten out alive.")
    raw_input("press [enter] >")
    print ("Are you sure you want to enter the dungeon?")

    pcmd = raw_input("please choose [y] or [n] >")

    # the player can choose yes or no
    if (pcmd == "y"):
        print ("You walk down the stairs. It's getting dimmer and dimmer...")
        raw_input("press [enter] >")
        dungeonEntry()
    else:
        print ("Good for you. I don't want to see more sacrifice...")
        pcmd = raw_input("press [enter] >")
        introStory() # repeat over and over until the player chooses yes!


def printGraphic(name):
    if (name == "title"):
        print ('___________________________________________________________________________________________')
        print ('                                                                                           ')
        print ('                                                                                           ')
        print ('||||||||    ||        ||  ||||     ||  ||||||||||  ||||||||||  ||||||||||  ||||     ||     ')
        print ('||     ||   ||        ||  || ||    ||  ||          ||          ||      ||  || ||    ||     ')
        print ('||      ||  ||        ||  ||  ||   ||  ||          ||          ||      ||  ||  ||   ||     ')
        print ('||      ||  ||        ||  ||   ||  ||  ||   |||||  ||||||||||  ||      ||  ||   ||  ||     ')
        print ('||     ||    ||      ||   ||    || ||  ||      ||  ||          ||      ||  ||    || ||     ')
        print ('||||||||      ||||||||    ||     ||||  ||||||||||  ||||||||||  ||||||||||  ||     ||||     ')
        print ('                                                                                           ')
        print ('                                                                                           ')
        print ('||   |||   ||    |||||||     ||||||||||   ||||||||||   ||||||||   ||||||||||   ||||||||||  ')
        print ('||  || ||  ||   ||     ||    ||      ||   ||      ||      ||      ||      ||   ||      ||  ')
        print ('||  || ||  ||  ||       ||   ||      ||   ||      ||      ||      ||      ||   ||      ||  ')
        print ('|| ||   || ||  |||||||||||   ||||||||||   ||||||||||      ||      ||      ||   ||||||||||  ')
        print ('|| ||   || ||  ||       ||   ||    ||     ||    ||        ||      ||      ||   ||    ||    ')
        print ('||||     ||||  ||       ||   ||      ||   ||      ||   ||||||||   ||||||||||   ||      ||  ')
        print ('                                                                                           ')
        print ('___________________________________________________________________________________________')

    if (name == "health"):
        print ('           ')
        print (' |||  |||  ')
        print ('|||||||||| ')
        print (' ||||||||  ')
        print ('   ||||    ')
        print ('    ||    ')
    
    if (name == "death"):
        print ('   ||||||||||||||    ')
        print ('  ||            ||   ')
        print (' ||  |||    |||  ||  ')
        print ('||  || ||  || ||  || ')
        print (' ||  |||    |||  ||  ')
        print ('  ||     ||     ||   ')
        print ('   ||          ||    ')
        print ('   || || || || ||    ')
        print ('   ||          ||    ')
        print ('    ||||||||||||     ')
        print ('                     ')
     
    if (name == "slime"):
        print ('                         ')
        print ('      |||||||||||        ')
        print ('    ||            ||     ')
        print ('   ||              ||    ')
        print ('  ||    ||    ||     ||  ')
        print ('  ||                  || ')
        print (' ||                  ||  ')
        print ('  ||||||||||||||||||||   ')
        print ('                         ')

    if (name == "lizard"):
        print ('')
        print ('                ||')
        print ('              ||||')
        print ('             || ||')
        print ('            ||  ||')
        print ('            ||||||')
        print ('              ||')
        print ('              ||||||||||||')
        print ('             |||           ||')
        print ('           || ||  ||        ||') 
        print ('      |||||   ||             ||')
        print ('      ||      ||               ||')
        print ('       |||||||||||||||         ||')
        print ('              ||     ||   ||||  ||')
        print ('              ||     ||  ||   || ||')
        print ('              ||     ||  ||  ||   ||')
        print ('             ||||   || ||   ||     ||')
        print ('          |||   ||||||||  ||        ||||                   ||| ')
        print ('            ||||||||||||||              |||            |||| ')
        print ('              ||        |||     |||||||    ||||     ||||||')
        print ('              ||          |||  ||      |||     ||||||||')
        print ('              ||         || |||        ||||||||||||||')
        print ('              ||          ||   ||    ||')
        print ('              ||      ||||||    ||   ||')
        print ('              ||   ||||||||  |||||   ||')
        print ('              ||        |||||||||||||')
        print ('                                                ')

    if (name == "ghost"):
        print ('')
        print ('             |||||||||||')
        print ('           ||           ||')
        print ('          ||              ||')
        print ('         ||    |||   |||    ||')
        print ('         ||    |||   |||    ||')
        print ('   ||||||||                 ||||||||||')
        print (' |||       ||      |||       ||      ||')
        print ('  ||  ||||| ||     ||||      || ||||  ||')
        print ('   |||       ||     |||       ||    |||')
        print ('              ||||            ||')
        print ('               ||||           ||')
        print ('                   ||||        ||')
        print ('                      |||||||    |||||')
        print ('                            |||||||||||||||')
        print ('')
        
    if (name == "chest"):
        print ('')
        print ('       |||||||||||||||||||||||')
        print ('     ||                ||||   ||')
        print ('   ||                ||||      ||')
        print (' ||       ||        ||||        ||')
        print ('|||||||||||||||||||||||||||||||||||')
        print ('||        ||       ||||          ||')
        print ('||                 ||||          ||')
        print ('||                 ||||          ||')
        print ('|||||||||||||||||||||||||||||||||||')
        print ('')
        
        


        


def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens
