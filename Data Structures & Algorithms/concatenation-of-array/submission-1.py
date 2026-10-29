class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #SOLN1:
        #return nums + nums

        #SOLN2:
        concatenated_array = []
        
        # want to itterate through nums twice
        for i in range(2):
            for val in nums:
                concatenated_array.append(val)
        return concatenated_array
        