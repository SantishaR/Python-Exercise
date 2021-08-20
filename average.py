# Write a method average_of_three(num1, num2, num3) 
# that returns the average of three numbers

def average_of_three(num1, num2, num3):

    sum_total = int(num1) + int(num2) + int(num3)
    average = sum_total / 3
    # print output using string formatting
    print("The average of %d, %d, %d is %d " % (num1, num2, num3, average))
    return average


average_of_three(58, 2, 8)



