# Doubler
# Write a method doubler(numbers) that 
# takes an array of numbers and returns a new array
# where every element of the original array 
# is multiplied by 2.

def doubler():
   numbers = [1, 2, 3, 4, 5]
   doubled_numbers = []

   for n in numbers:
    new_number = n * 2
    doubled_numbers.append(new_number)

   print(doubled_numbers)


doubler()
