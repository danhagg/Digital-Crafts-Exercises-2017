"""
If you want to make it safe, you first write the new data into a temporary file in the same folder, and then rename the temporary file onto the original file. That way you will not lose any data even if something happens in between.
"""

import json
 
# phoneDict = {"Gandalf": 6666, "Boris": 5555, "Keyzer": 4444}
phoneDict = {}

# while loop needed for entire duration of choices for saving etc
while True:


    choice = input("Please enter a number from 1 to 5. What would you like to do?: \n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit WITHOUT saving\n6. Save entries\n7. Restore entries\n\nChoice 1- 7?  ")

    # Lookup
    if choice == "1":
        print("You chose 1")
        name = input("Please enter a name: ")
        if name in phoneDict.keys():
            print("{0}\'s phone number is {1}".format(name, phoneDict[name]))
        else:
            print("You entered {0}. That is not a name in the phonebook!".format(name))

    # New entry
    if choice == "2":
        print("You chose 2")
        newName = input("Please enter a name for the entry: ")
        newNumber = input("Please enter a number for the entry: ")
        newEntry = {newName: newNumber}
        phoneDict.update(newEntry)
        print("The new phonebook looks like this\n {0}".format(phoneDict))

    # Delete an entry
    if choice == "3":
        print("You chose 3")
        delName = input("Please enter the name of who would you like to delete: ")
        del phoneDict[delName]
        print("You have deleted {0} and the new phonebook looks like this\n {1}".format(delName, phoneDict))

    # Clear entries
    if choice == "4":
        print("You chose 4: Here is the current phonebook: ")
        print(phoneDict)
        print()

    # Quit program.
    if choice == "5":
        print("You chose 5 = QUIT")
        break

     # Save entries
    if choice == "6":
        print("You chose 6")
        with open('data.json', 'w') as f:
            json.dump(oldphoneDict, f)

    # Restore entries
    if choice == "7":
        print("You chose 7")
        with open('data.json', 'r') as f:
            oldPhoneDict = json.load(f)
            newPhoneDict = oldPhoneDict.update(phoneDict)
            print(newPhoneDict)




