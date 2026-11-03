class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Intuition
        The problem requires finding the maximum count of consecutive 
        ones in a binary array. 
        
        One approach could be to iterate through the array and keep track 
        of the current count of consecutive ones while updating the maximum 
        count seen so far.
        
        Approach
        Initialize two variables: max_count to keep track of the maximum 
        count of consecutive ones, and curr_count to keep track of the 
        current count of consecutive ones.
        
        Iterate through the array:
        If the current element is 1, increment curr_count.
        If the current element is 0, update max_count with the 
        maximum of max_count and curr_count, and reset curr_count to 0.
        After the loop, update max_count one last time to account for 
        the consecutive ones at the end of the array.
        
        Return max_count.
        """
        max_count = curr_count = 0
        
        for num in nums:
            if num == 1:
                curr_count += 1
                max_count = max(max_count, curr_count)
            else:
                curr_count = 0
        return max_count