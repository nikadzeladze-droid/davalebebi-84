arr = [1,2,3,4,5,6,7]
search_name = input("Enter name to find index: ")

if search_name in arr:
    print("Index:", arr.index(search_name))
else:
    print("not index in list")
