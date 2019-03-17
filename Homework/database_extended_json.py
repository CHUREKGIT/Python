import json

data=[]

with open('database.json') as database:
    data = json.load(database)
    print(f"This is your database:\n{data['users']}")

#function to get choice from user
def choices():
 global choice
 choice = int(input("What do you want to do:\n[0] - exit program\n[1] - add new user\n[2] - delete existing user\n[3] - check user in database\n[4] - check number of user in database\n"))

#function to add new object to database and to json
def adding():
    name = input("Please give me a name\n")
    lastname = input("Please give me a lastname\n")
    phonenumber = input("Plase give me a phonenumber\n")

    #converst to disct
    user = dict(name = name, lastname = lastname, phone = phonenumber)

    data['users'].append(user)

    #updating file
    with open ('database.json', 'w') as database:
        json.dump(data, database)

    #confirmation
    print(f"{user} has been added to database")
    choices()


#function to removing objects from database
def remover():
    print(data)

    name_delete = (input("Provide user name to delete\n"))

##I cant find idea for validation here :(

    for dict in data['users']:
        for key, value in dict.items():
            if value == name_delete:
                dict.clear() #only this working. del dict doesnt. I dont know why :(

                # updating file
                with open('database.json', 'w') as database:
                    json.dump(data, database)
                #confirmation
                print(f"User has been deleted\n")
                break

    choices()

def checker():
    finder = int(input("[1] - find by name\n[2]-find by last name\n[3]-find by phonenumber\n[0]-back to previous menu\n"))
    if finder == 1:
        name = input("Give me a name to find\n")
        for dictionary in data["users"]:
            if dictionary["name"] == name:
                print(dictionary)
                break
        else:
            print("I can't find user with this name\n")


    if finder == 2:
        lastname = input("Give me a lastname to find\n")
        for dictionary in data["users"]:
            if dictionary["lastname"] == lastname:
                print(dictionary)
                break
        else:
            print("I can't find user with this lastname\n")

    if finder == 3:
        phonenumber = input("Give me a phonenumber to find\n")
        for dictionary in data["users"]:
            if dictionary["phone"] == phonenumber:
                print(dictionary)
                break
        else:
            print("I can't find user with this phonenumber\n")

    if finder == 0:
        choices()

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
        print(f"Our database has {len(data['users'])} users")
        choices()