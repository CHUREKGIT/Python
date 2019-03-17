#function to get choice from user
def choices():
 global choice
 choice = int(input("What do you want to do:\n[0] - exit program\n[1] - add new user\n[2] - delete existing user\n[3] - check user in database\n[4] - check number of user in database\n"))

#function to add new object to database
def adding():
    name = input("Please give me a name\n")
    lastname = input("Please give me a lastname\n")
    phonenumber = input("Plase give me a phonenumber\n")
    user = dict(name = name, lastname = lastname, phone = phonenumber)
    database.append(user)
    print(f"{user} has been added to database")
    choices()

#function to removing objects from database
def remover():
    print(database)
    number_remove = int(input("Provide number user to delete\n"))
    database.remove(database[number_remove])
    print(f"User has been deleted\n")
    choices()

#function to checking if name/lastname/phonenumber is in database
def checker():
    finder = int(input("[1] - find by name\n[2]-find by last name\n[3]-find by phonenumber\n[0]-back to previous menu\n"))
    if finder == 1:
        name = input("Give me a name to find\n")
        for dictionary in database:
            if dictionary["name"] == name:
                print(dictionary)
            else:
                print("I can't find user with this name\n")
                break

    if finder == 2:
        lastname = input("Give me a lastname to find\n")
        for dictionary in database:
            if dictionary["lastname"] == lastname:
                print(dictionary)
            else:
                print("I can't find user with this lastname\n")
                break
    if finder == 3:
        phonenumber = input("Give me a phonenumber to find\n")
        for dictionary in database:
            if dictionary["phone"] == phonenumber:
                print(dictionary)
            else:
                print("I can't find user with this phonenumber\n")
                break
    if finder == 0:
        choices()


#our database
database = []

#start program
choices()

#main functionality
while choice > 0:
    if choice == 1:
        adding()
    if choice == 2:
        remover()
    if choice == 3:
        checker()
    if choice == 4:
        print(f"Our data base has {len(database)} users")
        choices()

