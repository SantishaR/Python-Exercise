# Fizz Buzz
# Write a method fizz_buzz(max)
# that takes in a number max and returns an array
# containing all numbers greater than 0 and less than max
# that are divisible by either 4 or 6, but not both.


def fizz_buzz(max):
    result = []

    for n in range(1, max):
       if (n % 4 == 0 or n % 6 == 0) and not(n % 4 == 0 and n % 6 == 0):
           result.append(n)
    return result


print(fizz_buzz(25))
