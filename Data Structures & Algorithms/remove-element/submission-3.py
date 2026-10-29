# cases to consider:
# nums = [], [val], [val, val, val], [#], [#, #, #]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # in-place : modify the given array nums, dont create a new one
        # only first k elements of nums cant contain elements = val
        # => swap in place elements equal to val with an element from the end of the list

        p1 = 0
        p2 = len(nums)-1

        # inefficient: sorting nums for all elements equal to val in one spot
        # solution -  position p2 to start at value != val 
        #           check that this condition is satisfied prior to checking index p1 and swapping 
        while p1 < p2:
            if nums[p2] == val and p2 > p1:
                p2 -= 1
            else:
                if nums[p1] == val:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p2 -= 1
                p1 += 1
        # regular case: nums[p1] == last non-val element
        # case: nums = [], [val], [val, val, val]
        #   result p1 = p2 = 0 after while loop completes
        #   nums[p1] == val or DNE
        if len(nums) >= 1 and nums[p1] != val:
            return p1 + 1
        return p1
        
        