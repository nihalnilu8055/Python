a=0
num=6
for i in range (1,num+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(1,end=" ")
        else:
            print(a+i-1,end=" ")    
    print()        