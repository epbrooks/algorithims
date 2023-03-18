# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’

def split_swap(string):
    length = len(string)
    midpoint = (length + 1) // 2

    first_half = string[:midpoint]
    second_half = string[midpoint:]

    return second_half + first_half

string1 =  'bbbaaa'
string2 = 'bbbbbcaaaaa'
result = split_swap(string1)
print(result)
result = split_swap(string2)
print(result)

# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

def unique_characters(string):
    for char in string:
        if string.count(char) > 1:
            return False
    else:
        return True


string1 = 'abcde'
string2 = 'aabcde'

result1 = unique_characters(string1)
result2 = unique_characters(string2)

print(result1)
print(result2)









