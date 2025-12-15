# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# two pointers
def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l+=1
            continue
        if not s[r].isalnum():
            r-=1 
            continue
        if s[l].lower() == s[r].lower():
            l+=1
            r-=1
            continue
        else:
            return False
    return True

# call
s = 'Race car'
print(isPalindrome(s))