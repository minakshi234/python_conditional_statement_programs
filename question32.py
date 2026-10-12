attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible due to marks")
else:
    print("Not eligible due to attendance")