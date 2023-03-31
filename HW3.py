# When given a list, the program should return a list of all the elements
# below the original list’s arithmetical mean. The arithmetical mean is the
# sum of all elements divided by the number of elements.

def below_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return [n for n in numbers if n < mean]


numbers = [1, 3, 5, 6, 4, 10, 2, 3]
result = below_mean(numbers)
print(result)


# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest(numbers):
    lowest = float('inf')
    second_lowest = float('inf')
    for n in numbers:
        if n < lowest:
            second_lowest = lowest
            lowest = n
        elif n < second_lowest:
            second_lowest = n
    return lowest, second_lowest


numbers = [198, 3, 4, 9, 10, 9, 2]
result = find_two_lowest(numbers)
print(result)




