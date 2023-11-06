l1=["abcd","a",1,11]
l2=["a",11,150.5]
a=[]
i=0
while i<len(l1):
    if l1[i] in l2:
        a.append(l1[i])
    i+=1
print(a)  
