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

# to get user input // Correction position of variable name
name = input("Enter a name:")
print("Searching " + name + " in databse, please wait...")


# loop
for elem in birthdayList:

    # search name & birthday

    name = elem['name']
    birthday = elem['birthday']

    if name == elem:
        print("name = " + name)
        print("Birthday = " + birthday)

    birthdayDictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])
