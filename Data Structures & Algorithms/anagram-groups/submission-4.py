class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
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
        '''
        groups={}
        for s in strs:
            key=[0]*26
            for c in s:
                key[ord(c)-ord('a')]+=1
            key=tuple(key)
            if key not in groups:
                groups[key]=[]
            groups[key].append(s)

        return list(groups.values())