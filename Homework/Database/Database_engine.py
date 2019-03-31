from Database import Database

Database()
choice = int(input("What do you want to do:\
\n[0] - exit program\
\n[1] - add new user\
\n[2] - delete existing user\
\n[3] - check user in database\
\n[4] - check number of user in database\n"))


#main functionality
while choice > 0:
    if choice == 1:
        Database.adding()
    if choice == 2:
        Database.remover()
    if choice == 3:
        Database.checker()
    if choice == 4:
        Database.length_checker()
    choice = int(input("What do you want do next?\n"))