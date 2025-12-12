from collections import Counter

def firstUniqChar(s):
        count = Counter(s)
        for index,char in enumerate(s):
            if count[char] == 1:
                return index
        return -1

# llamar la funcion
s = "leetcode"
print(firstUniqChar(s))