# name="muhammed nihal"
# c=name.title()
# print(c)


name=input("enter ur name: ")
words=name.split()


for i in range(len(words)):
        words[i]=words[i].title()


l=" ".join(words)
print(l)
