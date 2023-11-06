def count(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Upper case char:",upper)
    print("Lower case char:",lower)
string = input("enter a string: ")
count(string)