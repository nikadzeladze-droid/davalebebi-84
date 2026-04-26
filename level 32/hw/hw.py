# 2) კომენტარებით ახსნა

# .append() -> ამატებს ახალ ელემენტს სიის ბოლოში
# .insert(index, value) -> ამატებს ელემენტს მითითებულ პოზიციაზე
# .pop() -> შლის ელემენტს სიიდან (თუ ინდექსი არ მივუთითეთ, შლის ბოლოს)




numbers = [10, 20, 30, 40, 50]
print(len(numbers))




nums = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    nums.append(num)

print(nums)




colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()

print(colors)




animals = ["dog", "cat", "elephant", "lion"]

animals.insert(1, "monkey")

print(animals)




students = []

for i in range(3):
    name = input("შეიყვანე სტუდენტის სახელი: ")
    students.append(name)

students.insert(0, "Teacher")
students.pop() 

print(len(students))
print(students)