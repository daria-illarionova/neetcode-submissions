class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (complement) nums[i] = target - nums[j]
        # keep track of the complement & index of each value in nums
        complement_dict = {}

        # simultaneously populate complement_dict 
        # & determine if the complement of the current value exists
        for index, value in enumerate(nums):
            # compute the complement of current value
            complement = target - value
            # if the current value is in complement_dict => complement exists
            # return the index of complement & current index
            if value in complement_dict:
                # values in complement_dict will have smaller index's 
                # than current index as they were computed earlier
                # satisfying return requirement i < j & i != j
                return [complement_dict[value], index]
            # if complement not currently in dict, add it along with the index
            complement_dict[complement] = index
        
        return [None]



        
        