class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_set = set(nums)

        if len(nums) > len(nums_set):
            return True
        else:
            return False

        
        ''' Solution 1
        unique = []

        for x in nums:
            if x not in unique:
                unique.append(x)
            else:
                return True
        return False'''