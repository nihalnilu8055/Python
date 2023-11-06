# num=[-2,5,8,-9,-7,0,1,6]
# pos=list(filter(lambda x:x>0,num))
# print(pos)



# def vowels(char):
#     vowel="AEIOUaeiou"
#     return char in vowel
# ip=input("enter a strg: ")
# check=list(filter(vowels,ip))
# print("".join(check))


ip=input("enter a strg: ")
check=list(filter(lambda x:x in "AEIOUaeiou",ip))
print("".join(check))