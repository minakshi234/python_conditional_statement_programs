choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")