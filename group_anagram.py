# 49. Group Anagrams
from collections import Counter
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        orderedS = "".join(sorted(s))
        anagrams[orderedS].append(s)
    return list(anagrams.values())
                
            

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))