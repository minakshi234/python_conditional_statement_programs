role = input("Enter role: ")

match role.lower():
    case "admin":
        print("Full access")
    case "user":
        print("Normal access")
    case "guest":
        print("Limited access")
    case _:
        print("Invalid role")