def removeFirstLetter(s):
    return s[1:]


spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=removeFirstLetter)
print(spam)