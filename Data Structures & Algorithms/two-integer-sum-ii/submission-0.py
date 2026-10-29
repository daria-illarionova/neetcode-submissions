class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                # case: sum is larger than target, update r ptr to next smaller value
                r -= 1
            elif numbers[l] + numbers[r] < target:
                # case: sum is smaller than target, update l ptr to next larger value
                l += 1
            else:
                return [l+1, r+1]
        