class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        s=set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
            
