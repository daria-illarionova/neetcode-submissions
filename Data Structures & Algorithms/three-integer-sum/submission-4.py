class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # NOTE: The output should not contain any duplicate
        result = set()

        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > -(nums[i]):
                    k -= 1
                elif nums[j] + nums[k] < -(nums[i]):
                    j += 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    result.add(tuple(triplet))
                    j += 1
                    k -= 1
        return [list(i) for i in result]