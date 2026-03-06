# List operations
Numbers = []

while True:
    print("-----Menu-----")
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")

    choice = int(input("Enter your choice (1-4) : "))

    if(choice == 1):
        num = int(input("Enter an integer to add : "))
        Numbers.append(num)
        print("Added Successfully!")

    elif(choice == 2):
        if not Numbers:
            print("List is empty!")
        else:
            num = int(input("Enter an integer to add : "))
            if num in Numbers:
                Numbers.remove(num)
                print("Removed Successfully!")
            else:
                print("Element not found!")

    elif(choice == 3):
        print("Current list :")
        print(Numbers)

    elif(choice == 4):
        print("Exiting program...")
        break

    else:
        print("Invalid Choice!")