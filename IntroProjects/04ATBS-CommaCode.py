# Comma Code
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string wit
# h all the items separated by a comma and a space, with and inserted before the l
# ast item. For example, passing the previous spam list to the function would retu
# rn 'apples, bananas, tofu, and cats'. But your function should be able to work w
# ith any list value passed to it. Be sure to test the case where an empty list []
#  is passed to your function.

spam = ['apples', 'bananas', 'tofu', 'cats']


def comma_code(l):
    if (len(l) <= 0):
        return ""
    elif (len(l) == 1):
        return l[0]
    else:
        return ', '.join(l[:-1]) + " and " + l[-1]


print(comma_code(spam))