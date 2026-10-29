class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # shortest string should be used for loop to not index out of bands
        min_string = min(strs, key=len)

        # itterating through the indices in the shortest string,
        # compare that the value at that index is the same in every string
        # if the values are not equal, return the resulting prefix
        # otherwise append the value at that index to the resulting prefix, 
        # once every string in the list has been checked to have it. 
        for index in range(len(min_string)):
            for string in strs:
                if string[index] != min_string[index]:
                    return prefix
            prefix += min_string[index]
        return prefix


        

        