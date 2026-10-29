class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Let k: the number of elements in nums which are not equal to val.
        Return k
        Modify nums so that the first k elements of nums contain the elements
        which are not equal to val.
        - Remove all occurrences of val in nums in-place
        - Order of elements & size of nums can be changed
        - Not important: remaining elements in nums after first k elements 

        Edge Cases: 
        []
        [val]
        [non-val]

        Key Idea: Keep a pointer (K) referencing an index such that 
        the next time we find a non-val value, we can simply copy it into this index, 
        and then update pointer (K) by 1 to the right. 
        """
        k = 0

        for value in range(len(nums)):
            if nums[value] != val:
                nums[k] = nums[value]
                k += 1
        return k
        