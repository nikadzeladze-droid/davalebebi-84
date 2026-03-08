word = "sigma"


symbol = input("Enter a symbol: ")


if symbol in word:
    index = word.index(symbol)
    print(symbol , index)
else:
    print("This symbol is not in word")