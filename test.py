def duplicate_encode(word):
    letters = []

    for i in range(len(word)):
        if word.count(word[i]) > 1 and word[i] not in letters:
            letters.append(word[i])
    for i in letters:
        word = word.replace(i, ')')
    for i in range(len(word)):
        if word[i] != ')':
            word = word.replace(word[i], '(')
    return word


word = duplicate_encode('Success')
print(word)
