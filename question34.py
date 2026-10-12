year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year and Century year")
elif year % 100 == 0:
    print("Century year but not Leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Neither Leap year nor Century year")