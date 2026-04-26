
# 2) კომენტარებით ახსნა

# return keyword გამოიყენება ფუნქციიდან მნიშვნელობის დასაბრუნებლად.

# print() და return განსხვავდება:
# print() მხოლოდ ბეჭდავს პასუხს
# return აბრუნებს პასუხს და შეგვიძლია შევინახოთ ცვლადში





# 3)
def tuff_list(numbers):
    product = 1

    for num in numbers:
        product *= num

    return product

print(tuff_list([2, 3, 4]))





# 4) 

def first_function(num):
    return num

def second_function(num):
    return num * 2

answer = second_function(first_function(7))

print(answer)