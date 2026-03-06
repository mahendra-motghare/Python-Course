# Cricket_list_operations

Cricket_players = []

while True:
    print("-----Menu-----")
    print("1. Add Player")
    print("2. Remove Player")
    print("3. Display Players")
    print("4. Quit")

    choice = int(input("Enter your choice (1-4): "))

    if(choice == 1):
        if(len(Cricket_players) < 11):
            player = input("Enter player name to add: ")
            Cricket_players.append(player)
            print("Player Added Successfully!")
        else:
            print("Team already has 11 players!")

    elif(choice == 2):
        if not Cricket_players:
            print("Player list is empty!")
        else:
            player = input("Enter player name to remove: ")
            if player in Cricket_players:
                Cricket_players.remove(player)
                print("Player Removed Successfully!")
            else:
                print("Player not found!")

    elif(choice == 3):
        print("Current Players List:")
        print(Cricket_players)

    elif(choice == 4):
        print("Exiting program...")
        break

    else:
        print("Invalid Choice!")