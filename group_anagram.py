# 49. Group Anagrams
def groupAnagrams(strs):
    mainDict = {}
    elements = 0;
    anagrams = []

    for index,string in enumerate(strs):

        countDict = {}
        find = False

        for words in string:
            if words in countDict:
                countDict[words] = countDict[words] + 1
            else:
                countDict[words] = 1

        if index == 0:
            mainDict[elements] = countDict.copy()
            anagrams.append([])
            anagrams[elements].append(string)
        else:
            for y in range(len(mainDict)):
                if countDict == mainDict[y]:
                    find = True;
                    anagrams[y].append(string)
                    break
            if find == False:
                elements += 1
                anagrams.append([])
                anagrams[elements].append(string)
                mainDict[elements] = countDict.copy()
    return anagrams
        
            
            

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))