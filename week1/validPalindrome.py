# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# two pointers
def isPalindrome(s):
        s = s.lower()
        a = 0
        b = len(s) - 1
        while a < b:
            if not s[a].isalnum():
                a+=1 
                continue
            if not s[b].isalnum():
                b-=1
                continue
            if s[a] != s[b]:
                return False
            a+=1
            b-=1
        return True

# call
s = 'Race car'
print(isPalindrome(s))