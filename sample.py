s="hello"
chars = list(s)
index = []
vowels = []

for i in range(len(chars)):
    if chars[i] in ['a','e','i','o','u']:
        vowels.append(chars[i])
        index.append(i)

vowels = vowels[::-1]
final = []

ind = 0
for i in range(len(chars)):
    if i in index:
        final.append(vowels[ind])
        ind += 1
    else:
        final.append(chars[i])

str1 = ""
x=str1.join(final)

print(x)





