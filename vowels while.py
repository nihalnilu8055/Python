word=input("enter  word: ")
v="a","e","i","o","u"
count=0
i=0
while word:
    if i in v:
        count+=1
    i+=1        
print(count)            