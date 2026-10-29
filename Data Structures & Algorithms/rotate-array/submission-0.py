class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # 1) reverse the entire array
        L, R = 0 , len(nums) - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L, R = L + 1, R - 1

        # 2) reverse the first k elements in array (from 0 to k -1)
        L, R = 0 , k - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L, R = L + 1, R - 1

        # 3) reverse the remaining portion of elements in the array (from k to the end of the array)
        L, R = k , len(nums) - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L, R = L + 1, R - 1


        