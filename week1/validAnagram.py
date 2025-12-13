# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
from collections import Counter

def isAnagram(s,t):
    return Counter(s) == Counter(t)

# call
s = 'anagram'
t = 'nagaram'
print(isAnagram(s,t))