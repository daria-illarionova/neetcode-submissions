class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = 0

        w_len = 0
        
        for R in range(len(nums)):
            if nums[L] == 0:
                L += 1
            else:
                if R == len(nums) - 1:
                    w_len = max(w_len, (R - L)+ 1)
                elif nums[R+1] == 0:
                    w_len = max(w_len, (R - L)+ 1)
                    L = R + 1
        return w_len