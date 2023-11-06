num=[3,8,12,7,6,10,21,15]
sum=18

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == sum:
            print(f"({num[i]}, {num[j]})")
