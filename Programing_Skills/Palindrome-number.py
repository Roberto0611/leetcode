'''
Given an integer x, return true if x is a palindrome, and false otherwise.
leetcode problem link: https://leetcode.com/problems/palindrome-number/description/

Follow up: Could you solve it without converting the integer to a string? (completed)
'''

# Solution
def isPalindrome(x):
    # if negative no palindrome
    if 0 > x:
        return False
    
    # if less tan 10 no palindrome
    if x < 10:
        return True

    digits = []

    # while loop
    while x != 0:
        digits.append(x%10)
        x = x//10

    reversDigits = digits[:]
    reversDigits.reverse()

    return digits == reversDigits

# Call and test the function
number = 122
print(isPalindrome(number)) 