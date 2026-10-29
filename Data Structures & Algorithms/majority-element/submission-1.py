class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # important: 
        #   1. frequency every char occurs
        #   2. the max frequency

        # cases: [], [#], [...]

        element_freq = {}

        for char in nums:
            if char not in element_freq:
                element_freq[char] = 1
            else:
                element_freq[char] += 1
    
        max_key = max(element_freq, key=element_freq.get)
        return max_key
        