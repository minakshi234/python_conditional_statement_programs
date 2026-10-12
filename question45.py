choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Sandwich")
    case 4:
        print("Pasta")
    case _:
        print("Invalid choice")