# Your input is a list of integers, and you have to reorder its entries so that
# the even entries appear first. You are required to solve it without allocating
# additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def reorder_even(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 == 1]
    return evens + odds


numbers = [7, 3, 5, 6, 4, 10, 3, 2]
result = reorder_even(numbers)
print(result)


# Write a program that takes as input a list of digits encoding a nonnegative decimal
# integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_integer(digits):
    n = int(''.join(map(str, digits)))
    n += 1
    return list(map(int, str(n)))


digits = [1, 2, 9]
result = increment_integer(digits)
print(result)



