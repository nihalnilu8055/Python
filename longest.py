sent=input("enter a sent:")
words=sent.split()
longest= ""
for i in words:
    if len(i)> len(longest):
        longest=i
print(longest)        