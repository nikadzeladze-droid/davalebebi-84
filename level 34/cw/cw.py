def greet(name):
    print("Hello World!")
    print(f"Hello {name}")
greet("Giorgi")

def double(number):
    return number * number
print(double(5)) 

def checkOdd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"
print(checkOdd(7))

def BMI(height, weight):
    return weight / (height * height)
print(BMI(1.75, 70))