n = int(input("Enter number: "))

if n >= 0 and n <= 9:
    print("Single digit")
elif n >= 10 and n <= 99:
    print("Double digit")
elif n >= 100 and n <= 999:
    print("Three digit")
else:
    print("Other")