class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Return k: the number of unique elements in nums
        The first k elements of nums should contain the unique numbers in sorted
        order. The remaining elements beyond index k - 1 can be ignored.

        - remove duplicates in-place
        - keep the same relative order
        
        Cases: 
        - smallest possible input: [1]
        """
        '''
        The final/resulting array has the first unique element in the "first"
        index/position, second unique element in the second spot ...
        Goal -  Want the x'th unique element in the x'th index 
        In the array, need to keep track of the index where the next unique element 
        has to go. (Consider the indices occupied by duplicate values to be open)
        pointers: current position/value in nums, the next available index for a
        unique value'''

        # k: the number of unique elements in nums / the ptr to track the position of the last unique element
        k = 0
        i = 1

        while i < len(nums):
            if nums[i] > nums[k]:
                k += 1
                # in-place swap
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            else:
                i += 1
        # Accounting for Pythons zero-based indexing
        return k+1