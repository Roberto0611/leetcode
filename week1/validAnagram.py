# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# approach 1
def isAnagram(s,t):
    countS = {}
    countT = {}

    for letra in s:
        countS[letra] = countS.get(letra,0) + 1
        
    for letra in t:
        countT[letra] = countT.get(letra,0) + 1
    
    return countS == countT

# call
s = 'anagram'
t = 'nagaram'
print(isAnagram(s,t))