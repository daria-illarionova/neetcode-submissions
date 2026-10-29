class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [3,4,5,6]
        [1,1,1,1]
        smallest case: [+- x,+- y]
        """
        # Keep track of each number value and its corresponding indice
        # For repeated values, update index to the last index visited
        nums_dict = {}

        for x in range(len(nums)):
            nums_dict[nums[x]] = x

        # i + j = target => j = target - i
        # IF j exists in dictionary (and i!= j, meaning different index values), 
        # THEN this is a valid pair
        for i in range(len(nums)):
            j = target - nums[i]

            if j in nums_dict and nums_dict[j] != i:
                return [i, nums_dict[j]]
        return []
            
            
        