num = 0

while num >= 0:
    num = int(input("Enter a number: "))
    if num >= 0:
        print("Positive number entered")
    else:
        print("Negative number entered. Program stopped.")
        break