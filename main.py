rizz = 0
game_running = True
room = "starting"

while game_running:
    if room == "starting":
        print("You see a Derek standing in the cafeteria. What do you do?")
        print("1. Give him a chicken sandwich")
        print("2. Tickle him")
        print("3. Propose to him")

        answer = input("wyd: ")

    if answer == "1":
        room = "eating"
    elif answer == "2":
        room = "tickled"
    elif answer == "3":
        room = "rizz_check"
    else:
        print("wdym")

    if room == "rizz_check":
        if rizz >= 100:
            print("congrats you found Derek love")
            game_running = False
        else:
            print("He tells you he don't see you like that yet. Try again later")
            room = "starting"

    if room == "eating":
        rizz += 50
        print("He eats it in 7.38 seconds and looks happy")
        print("1. Give him another sandwich")
        print("2. Tickle him")
        print("3. Propose to him")

        answer = input("wyd: ")

    if answer == "1":
        room = "eating"
    elif answer == "2":
        room = "tickled"
    elif answer == "3":
        room = "rizz_check"
    else:
        print("wdym")

    if room == "tickled":
        rizz -= 5
        print("He looks at you weirdly.")
        print("1. Tickle him again")
        print("2. Give him a chicken sandwich")
        print("3. Propose to him")

        answer = input("wyd: ")
            
    if answer == "1":
        room = "tickled"
    elif answer == "2":
        room = "eating"
    elif answer == "3":
        room = "rizz_check"
    else:
        print("wdym")