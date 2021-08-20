# Is Palindrome

# A palindrome is a word that is spelled the same forwards
# and backwards.

# Write a method is_palindrome(word) that takes in a string word and 
# returns the true if the word is a palindrome, false otherwise.

def is_palindrome(word):
    # reversing a string using slice notation
    if word == word[::-1]:
        # print output using string formatting
        print("The word %s is a palindrome" % word)
    else:
        print("The word %s is not a palindrome" % word)


is_palindrome("Santisha")
is_palindrome("dad")


# method 2
def is_palindrome():

    pal_word = input("Enter the word and see if it is palindrome: ")

    if pal_word == pal_word[::-1]:
     print("This word is palindrome")
    else:
        print("This word is not palindrome")


is_palindrome()
