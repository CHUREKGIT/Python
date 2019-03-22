from database_extended_json_ENGINE import *

choice = int(input("What do you want to do:\
\n[0] - exit program\
\n[1] - add new user\
\n[2] - delete existing user\
\n[3] - check user in database\
\n[4] - check number of user in database\n"))


#main functionality
while choice > 0:
    if choice == 1:
        adding()
    if choice == 2:
        remover()
    if choice == 3:
        checker()
    if choice == 4:
        print(f"In your database are {len(data['users'])} users")
    choice = int(input("What do you want do next?\n"))