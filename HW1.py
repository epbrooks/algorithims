# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_digits(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i

    return total_sum


result = sum_of_digits(15)
print(result)


# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def max_number():
    values = [15, 45, 30]
    return max(values)


result = max_number()
print(result)


#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def odd_even_digits(num):
    even_digits = 0
    odd_digits = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
    return even_digits, odd_digits


even_digits, odd_digits = odd_even_digits(45690)


print(f'Even digits: {even_digits}')
print(f'Odd digits: {odd_digits}')




