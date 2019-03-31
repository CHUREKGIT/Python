import json

#show database
with open('database.json') as database:
    data = json.load(database)
    print(f"This is your database:\n{data['users']}")


#function to add new object to database and to json
def adding():
    name = input("Please give me a name\n")
    if name.isalpha():
        pass
    else:
        print("Name conatins number or special . Try again")
        name = input("Please give me a name\n")

    lastname = input("Please give me a lastname\n")
    if lastname.isalpha():
        pass
    else:
        print("Lastname conatins number or special . Try again")
        lastname = input("Please give me a name\n")
    try:
        phonenumber = int(input("Plase give me a phonenumber\n"))
    except ValueError:
        print("This not a number. Try again")
        phonenumber = int(input("Plase give me a phonenumber\n"))

    #converst to list
    user = [name, lastname, phonenumber]

    data['users'].append(user)

    #updating file
    with open ('database.json', 'w') as database:
        json.dump(data, database)

    #confirmation
    print(f"{user} has been added to database")

#function to removing objects from database
def remover():
    print(data)
    choice2 = int(input("How do you want delete user?\
\n by name -> press[0]\
\n by lastname -> press[1]\
\n by phonenumber -> press[2]\n"))

    if choice2 == 0:
        name_delete = (input("Provide user name to delete\n"))
        counter = 0
        for users in data['users']:
            if users[0] == name_delete:
                data['users'].remove(users)
                # updating file
                with open('database.json', 'w') as database:
                    json.dump(data, database)
                #confirmation
                print(f"User has been deleted\n")
                break
            else:
                counter +=1

            if counter == len(data['users']):
                print("I can't find this user in database")

    if choice2 == 1:
        lastname_delete = input("Provide lastname to detlete\n")
        counter = 0
        for users in data['users']:
            if users[1] == lastname_delete:
                data['users'].remove(users)
                # updating file
                with open('database.json', 'w') as database:
                    json.dump(data, database)
                # confirmation
                print(f"User has been deleted\n")
                break
            else:
                counter += 1

            if counter == len(data['users']):
                print("I can't find this user in database")
        if choice2 == 2:
            phone_delete = input("Provide phonenumber to detlete\n")
            counter = 0
            for users in data['users']:
                if users[2] == phone_delete:
                    data['users'].remove(users)
                    # updating file
                    with open('database.json', 'w') as database:
                        json.dump(data, database)
                    # confirmation
                    print(f"User has been deleted\n")
                    break
                else:
                    counter += 1

                if counter == len(data['users']):
                    print("I can't find this user in database")
def checker():
    finder = int(input("[1] - find by name\n[2]-find by last name\n[3]-find by phonenumber\n[0]-back to previous menu\n"))
    if finder == 1:
        name = input("Give me a name to find\n")
        for users in data["users"]:
            if users[0].upper() == name.upper():
                print(users)
                break
        else:
            print("I can't find user with this name\n")


    if finder == 2:
        lastname = input("Give me a lastname to find\n")
        for users in data["users"]:
            if users[1].upper() == lastname.upper():
                print(users)
                break
        else:
            print("I can't find user with this lastname\n")

    if finder == 3:
        phonenumber = input("Give me a phonenumber to find\n")
        for users in data["users"]:
            if users[2] == phonenumber:
                print(users)
                break
        else:
            print("I can't find user with this phonenumber\n")

    if finder == 0:
        return False