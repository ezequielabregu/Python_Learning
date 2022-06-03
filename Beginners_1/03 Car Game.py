command = "" # init variable
started = False


while True:
    command = input("--> ").lower() # con .lower todos los commnad se convierten en command.lower()

    if command == "start":
        if started:
            print("card is already started")
        else:
            started = True
            print("Car started..")
    elif command == "stop":
        if not started:
            print("Car is already sttoped")
        else:
            started == False
            print("Car Stopped...")
    elif command == "help":
        print("""
        start - start the car
        stop - stop the card
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I can't understand")