class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique = []

        for x in nums:
            if x not in unique:
                unique.append(x)
            else:
                return True
        return False