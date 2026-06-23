class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thisDict={}
        arr=[]
        final=[]

        for s in strs:
            for c in s:
                thisDict[c]=thisDict.get(c,0)+1            
            if thisDict not in arr:
                arr.append(thisDict)
                final.append([s])
            else:
                index=arr.index(thisDict)
                final[index].append(s)
            thisDict={}
        

        return final