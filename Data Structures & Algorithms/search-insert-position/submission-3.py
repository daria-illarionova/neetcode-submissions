class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        ''' Process: 
        With each iteration, "halve" the list by updating the left & right
        pointer to narow search to the right/left half of the list. 
        
        Stop when left and right pointers meet. 
        Note: The left and right pointers should reference the same index 
        on the last itteration, where we compare target to index value. 
        '''
        
        while left <= right:
            # Find the middle index (using integer division)
            mid = left + (right - left) // 2

            # Case: Target value found
            if nums[mid] == target:
                return mid

            # Case A/B: Target is smaller/greater than value (nums[mid])
            # Move the right/left pointer to the left/to the right, narrowing search to correct half of the list. 
            # Sub-Case: Target not in nums, on the last iteration deterime whether target should be to the left/right of index value.

            elif nums[mid] > target:
                if left == mid:
                    return mid
                else:
                    right = mid - 1
            else:
                if right == mid:
                    return mid + 1
                else: 
                    left = mid + 1
        