''''You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.'''
def mergeAlternately(word1: str, word2: str) -> str:  
    merged = ""
    
    if len(word1) == len(word2):
        i = 0
        while i < len(word1):
            merged += word1[i] + word2[i]
            i += 1
        return merged
    else:

        #Get lower
        if len(word1) > len(word2):
            lowerLen = len(word2)
            higher = word1
        else:
            lowerLen = len(word1)
            higher = word2

        i = 0
        while i < lowerLen:
            merged += word1[i] + word2[i]
            i += 1
        merged += higher[i:]
        return merged

# Llamar funcion
print(mergeAlternately("abcd","pq"))

