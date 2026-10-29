class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Prefix and Suffix Technique - pattern used to precompute cumulative 
        data (such as sums, products, minimums, or maximums) 
        across an array in O(n), allowing subsequent range or "except self"
        queries to be answered in O(1)

        • Prefix Array: Stores cumulative information from the start of 
        the array (index 0) up to the current index i.
        • Suffix Array: Stores cumulative information from the end of 
        the array down to the current index i (traversed in reverse).

        Note for Sums:  only require prefix array 
            RangeSum(L, R) = prefix[R + 1] - prefix[L]
            [4,2,7,3,5] => PA = [4, 6, 13, 16, 21]
        
        Note for Product: require both prefix and suffix array
            • prefix product array contains the product of all elements 
            to the left of i.
            • suffix product array containing the product of all elements 
            to the right of i.
            • multiply the corresponding prefix and suffix values for each
            index i: result[i] = prefix[i - 1] * suffix[i + 1]
        """
        # Creating 'empty' prefix and suffix array
        # Arrays are pre-populated with the same number of indices as nums,
        # in order to simplify populating both arrays at a particular index
        prefix_prod = [0] * len(nums)
        suffix_prod = [0] * len(nums)

        # Counter prev, keeps track of the final computed product of/up to previous index
        # Can easily compute the product of elements from 0 to current index by multiplying the previous index's final product with current index value. 
        # Init to 1, as multiplication by 1 has no effect on result. Can't be 0 as (0)(any #) = 0.
        prev = 1
        for p in range(len(nums)):
            curr_prod = prev * nums[p]
            prefix_prod[p] = curr_prod
            prev = curr_prod
        
        prev = 1
        for s in range(len(nums)-1, -1, -1):
            curr_prod = prev * nums[s]
            suffix_prod[s] = curr_prod
            prev = curr_prod

        output = [0] * len(nums)
        for i in range(len(nums)):
            # output[i] = prefix_prod[i -1] * suffix_prod[i + 1]
            # case: [i-1] when i = 0  & [i + 1] when i = n (n = len(nums) - 1) => IndexError 
            #   output[0] = suffix_prod[1] & output[n] = prefix_prod[n -1]
            if i == 0:
                output[i] = suffix_prod[i+1]
            elif i == len(nums) -1:
                output[i] = prefix_prod[i -1]
            else:
                output[i] = prefix_prod[i - 1] * suffix_prod[i + 1]
        return output