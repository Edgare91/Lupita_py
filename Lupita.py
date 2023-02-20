import json
# Import function to read Json File (data base on Json format (JavaScript Object Notation)

pathFile = "/Users/Edgar/Documents/GitHub/Lupita_py/birthday.json"
# Copy path right click on Json

# Try and catch errors

try:
    jsonFile = open(pathFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathFile)
    exit(-1)  # why -1??????


# Json file into a variable
birthdayList = json.load(jsonFile)

# An empty dictionary
birthdayDictionary = {}


# loop
for elem in birthdayList:

    # search name & birthday

    name = elem['name']
    birthday = elem['birthday']
    birthdayDictionary[name] = birthday

# to get user input
name = input("\nEnter a name: ")

# get a key value from the input in the new dictionary after the loop
# How can i concanete a string before the default else??
# (birthdayDictionary.get(name))


# to print a value in the dictionary by giving it a string with the name as the key
if name in birthdayDictionary:
    print(name + "'s birthday is: " + birthdayDictionary[name]+"\n")
else:
    print("Sorry this person is not a Lupita's friend :(\n")
