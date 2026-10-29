class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        Intuition: 
        Recall 2 SUM - looking for two values that sum up to target value 
        nums[j] + nums[k] == target

        3 SUM Objective: nums[i] + nums[j] + nums[k] == 0
                        => nums[j] + nums[k] == -(nums[i])
        -(nums[i]) is the target value
        
        Recall -  if <nums> is sorted, values are arranged from 
        smallest (on the left) to largest (on the right).
        Allows pointers to be placed in front of curr index only, instead of before & after. 

        Recall 2 SUM - 2 PTR approach at the start and end of a list
        """
        result = []

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
                    # NOTE: The output should not contain any duplicate triplets
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return result