mark=0
answer = input("How many months do we have in a year? ")
if answer == "12":
    print("Correct")
    mark +=1
else:
    print("incorrect")

answer = input("How many days do we have in a week? ")
if answer == "7":
    print("Correct")
    mark +=1
else:
    print("incorrect")
    
answer = input("How many days are there in a year? ")
if answer == "365":
    print("correct")
    mark +=1
else:
    print("incorrect")

print("mark=",mark)