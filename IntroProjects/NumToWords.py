import inflect


def myNumToStr(n):
    onesDigits = [
        'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Eleven', 'Twevle', 'Thriteen', 'Fourteen', 'Fifteen',
        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
    ]

    tensDigits = [
        'Twenty', 'Thrity', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty',
        'Ninety'
    ]
    if (n <= 19):
        return onesDigits[n]
    elif (n % 10 == 0):
        return tensDigits[int(n / 10) - 2]
    elif (n < 100):
        return tensDigits[int(n / 10) -
                          2] + " " + onesDigits[n - (int(n / 10) * 10)]


translator = inflect.engine()
numToTranslate = int(input("What number shall I say? "))
print(translator.number_to_words(numToTranslate))
print(myNumToStr(numToTranslate))
