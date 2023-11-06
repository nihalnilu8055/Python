
items=["apple","orange","milk","banana"]
a=input("enter items: ")
i=0
while i<len(items):
    if items[i]==a:
        print("already in list",a)
        break
    print(items[i])
    i+=1