#Naive vowel removal.

removeVowels = "EQuis sapiente illo autem mollitia alias corrupti reiciendis aut. Molestiae commodi minima omnis illo officia inventore. Quisquam sint corporis eligendi corporis voluptatum eos. Natus provident doloremque reiciendis vel atque quo. Quidem"

charToRemove = ['a', 'e', 'i', 'o', 'u']

print(removeVowels)
for char in charToRemove:
    removeVowels = removeVowels.replace(char, "")
    removeVowels = removeVowels.replace(char.upper(), "")
print(removeVowels)
