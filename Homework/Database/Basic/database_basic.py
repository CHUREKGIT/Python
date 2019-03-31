
def choices():
 global choice
 choice = int(input("What do you want to do:\n[0] - exit program\n[1] - add new name\n[2] - delete existing name\n[3] - check name in database\n[4] - check number of name in database\n"))

#function to add new object to database
def adding():
    name = input("Please give me a name\n")
    database.append(name)
    print(f"{name} has been added to database")
    choices()


#function to removing objects from database
def remover():
    print(database)
    name_remove = input("What do you want remove\n")
    database.remove(name_remove)
    print(f"{name_remove} has been deleted\n")
    choices


#function to checking if name is in database
def checker():
    name = input("Give me a name which you want to find")
    if name in database:
        print(f"Yes! We have this name in database. Its positon is {database.index(name)}")
        choices()
    else:
        print(f"I can't find {name} in database :( Sorry!")
        choices()




#our database
database = []

choices()
while choice > 0:
 if choice == 1:
     adding()
 if choice == 2:
   remover()
   choices()
 if choice == 3:
     checker()
 if choice == 4:
     print(f"Our data base has {len(database)} items")
     choices()

