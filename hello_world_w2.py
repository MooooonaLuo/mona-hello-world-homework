# Name: Jiayu Luo
# Assignment 1

myMac = {
    "model": "MacBook Pro",
    "size": 15,
    "year": 2015,
    "system": "macOS Big Sur",
    "systemVersion": "11.5.2",
    "memory": 16
}
# size in inch, memory in GB

myMug = {
    "color": "red",
    "brand": "Starbucks",
    "volume": 355
}
# volume in ml

myVitamin = {
    "brand": "Emergen-C",
    "netWeight": 273,
    "price": 9.99,
    "packNum": 30
}
# price in dollar, netWeight in g

myBed = {
    "brand": "Zinus",
    "size": "full",
    "heigh(inch)": 14,
    "material": "wood",
    "color": "dark brown"
}
# heigh in inch

# Assignment 2
{
    "name": "Momo",
    "type": "Yorkie",
    "age": 2,
    "gender": "female",
    "weight": 121
}
# weight in lbs

# Assignment 3

# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
fruit = raw_input("Enter your favorate fruit in plural: ")
name = raw_input("Enter a name: ")
adj = raw_input("Enter an adjective: ")
noun1 = raw_input("Enter a noun: ")
object1 = raw_input("Enter an object: ")


# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "In 2050, super-intelligent " + fruit + ", mistakenly created by scientists, " \
"have dominated the world. " + name + ", our bravest human leader, " \
"starts a revolution against the " + fruit + ". We create an army called " + adj + " " + noun1 + " and " \
"fight " + fruit + " with our newly designed weapon -- " + object1 + ". The war lasts for a decade, " \
"and we eventually take back our planet." 
     
# finally we print the story
print (story)