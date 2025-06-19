# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# imports
import re

# first approach
def isPalindrome(s):
    # RegEx to clean and format the string 
    cleanS = re.sub(r'[^a-zA-Z0-9]',"",s).lower()
    # reverse string and compare
    return cleanS[::-1] == cleanS

# call
s = 'Race car'
print(isPalindrome(s))