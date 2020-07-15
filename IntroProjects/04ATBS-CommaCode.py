spam = ['apples', 'bananas', 'tofu', 'cats']


def comma_code(l):
    if (len(l) <= 0):
        return ""
    elif (len(l) == 1):
        return l[0]
    else:
        return ', '.join(l[:-1]) + " and " + l[-1]


print(comma_code(spam))