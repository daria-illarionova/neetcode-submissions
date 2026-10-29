class Solution:
    import heapq

    def sortArray(self, nums: List[int]) -> List[int]:
        """ return nums in ascending order
            cases: [], [1], 
        """
        heapq.heapify(nums)

        n = len(nums)
        # pre-populate a list where indices of 0 to n-1 have 0's
        sorted_list = [0] * n

        # for loop get the smallest min at that time & places it at that position in the array
        # results in array being in ascending order
        # itterating n times to go through all of its valid indices
        for i in range(n):
            # get current min in log time
            minimum = heapq.heappop(nums)
            # set the value at index i (in array we want to populate) as the min
            sorted_list[i] = minimum 
        
        return sorted_list

        

        