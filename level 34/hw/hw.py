# 2) კომენტარებით ახსნა

# Custom ფუნქცია ნიშნავს ჩვენს მიერ შექმნილ ფუნქციას.
# მას ვიყენებთ იმისთვის, რომ კოდი გავამარტივოთ,
# თავიდან ავიცილოთ ერთი და იგივე კოდის გამეორება
# და საჭირო დროს მარტივად გამოვიძახოთ.


# პარამეტრი:
# პარამეტრი არის ცვლადი, რომელიც ფუნქციის შექმნის დროს იწერება ფრჩხილებში

# არგუმენტი:
# არგუმენტი არის რეალური მნიშვნელობა, რომელსაც ფუნქციის გამოძახებისას გადავცემთ

def greet(name):
    print(name)

greet("Giorgi") 


# 3) 

def add(a, b):
    return a + b

print(add(5, 7))


# 4)

def check_even(num):
    if num % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

check_even(8)
check_even(5)


# 5)

def square(num):
    return num ** 2

print(square(6))


# 6)

def big_text(text):
    return text.upper()

print(big_text("hello"))


# 7) 

def full_name(name, surname):
    print("მომხმარებლის სახელია", name, "ხოლო გვარია", surname)

full_name("Giorgi", "Beridze")