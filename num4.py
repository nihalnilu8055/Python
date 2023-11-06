a=6
for i in range (1,a+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(1,end=" ")
        else:
            print(2,end=" ")    
    print()        