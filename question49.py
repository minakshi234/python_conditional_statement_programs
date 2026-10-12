status = input("Enter result status: ")

match status.lower():
    case "pass":
        print("Congratulations")
    case "fail":
        print("Better luck next time")
    case "distinction":
        print("Excellent result")
    case _:
        print("Invalid status")