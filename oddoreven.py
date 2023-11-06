num=int(input("Enter a number:"))
if (num % 2)==0 :
   if (num % 3)  ==0:
      print("{0} is Even can divisible by 3".format(num))
   else:
      print("{0} is Even can not divisible by 3".format(num))
else:
   print("{0} is Odd".format(num))