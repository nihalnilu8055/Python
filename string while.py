list=input("enter a list: ").split()
i=0
while i<len(list):
    if 'e' in list[i]:
        print(list[i])
    i+=1
print(list)        