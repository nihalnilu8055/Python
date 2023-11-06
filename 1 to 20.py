for num in range(1,21):
    count=0
    for i in range(2,(num//2 + 1)):
        if(num % i == 0):
            count=count + 1
    if (count == 0 and num != 1):
        print(" %d" %num, end = '  ')