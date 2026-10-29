class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0

        while R < len(nums):
            count = 1
            while (R+1) < len(nums) and nums[R] == nums[R+1]:
                R += 1
                count += 1

            # R is moved/positioned at the index of last value in curr sequence
            
            # Want at most 2 copies of the curr value (there could be 1,2,3,... copies of the curr value in the sequence, reflected by <count>)
            # At most 2 copies => min(2, count)

            # TODO: populate index L with the "first 2 copies of the curr value"
            # NOTE - You don't actually need the literal first two elements from the sequence. All of the values in the curr sequence are the same. What's important is pasting this current sequences value at index L at most 2 times (recall ptr R is at one instance of this value), updating/incremeting L after each. 
            for i in range(min(2, count)):
                nums[L] = nums[R]
                L += 1
            
            # When for-loop terminates, move ptr R to the next/new sequence
            R += 1
        
        return L
        