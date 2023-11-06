sent=input("enter a sent: ")
words=sent.split()

for i in words:
    if i[0].isupper():
        print(i)