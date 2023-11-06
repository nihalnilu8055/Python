words = ['apple', 'banana', 'cherry', 'date']

for word1 in words:
    for word2 in words:
        common_letters = set(word1) & set(word2)
        if len(common_letters) > 0:
            print(f"('{word1}', '{word2}')")
