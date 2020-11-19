# Python program to print all permutations with 
# duplicates allowed 
def toString(l): 
    return ''.join(l) 
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(a, start_element_index, last_element_index): 
    if start_element_index==last_element_index: 
        print (''.join(a))
    else: 
        for i in range(start_element_index,last_element_index+1): 
            a[start_element_index], a[i] = a[i], a[start_element_index] 
            permute(a, start_element_index+1, last_element_index) 
            a[start_element_index], a[i] = a[i], a[start_element_index] # backtrack 
# Driver program to test the above function 
string = "A B C D"
a = string.split(' ')
n = len(a) 
permute(a, 0, n-1) 