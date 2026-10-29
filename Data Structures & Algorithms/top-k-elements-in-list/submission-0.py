from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        Intuition: 
        - Each number in <nums> occurs x times, where the max 
        'value of x'/frequency is the len(nums).
        Idea: Create a list where every index number corresponds to 
        a frequency. At each index, store the numbers that appear 
        that many times/have that index values frequency. 
        - Case where the frequency of a number in <nums> equals to len(nums)
        => List must have n indices 
        """

        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Populating freq array with len(nums) groups, +1 to counteract exclusive stop paramater
        freq = [[] for i in range(len(nums) + 1)]
        for num, f in freq_map.items():
            freq[f].append(num)
        
        result = []
        # Itterate through freq array from most to least frequent (backwards)
        # Start at the very last index: len(freq) -1
        # Stop (exclusive) set to 0 to end loop at index 1 since freq[0] = [] 
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

        

        