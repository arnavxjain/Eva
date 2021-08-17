from funcx import *

if __name__ == '__main__':
    user = User("Arnav", "Jain")
    customs(user.firstname)

    latitude, longitude = user.coordinates()

    run = True
    while run:
        command = str(input(f"{user.firstname} > "))

        if isGreeting(command):


        if command == "a-z":
            print("Entering Sleep Mode Now...")
            run = False
            break
