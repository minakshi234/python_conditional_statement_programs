n = int(input("Enter number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive but Odd")
else:
    print("Number is not positive")