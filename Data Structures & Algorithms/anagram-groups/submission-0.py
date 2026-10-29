from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Mapping charCount of each string to the list of anagrams
        # result = {}, using default dict where default value is a list
        # to avoid dealing with case where a key doesn't already exist 
        result = defaultdict(list)

        # For each str in strings array, 
        # create/use a list [0, ..,0] of len 26 to map the number of times 
        # a char appears in this string. 
        for s in strs:
            count = [0] * 26

            # Goal here is to 
            # 1) map chars a - z to indices 0 - 25 respectively
            # 2) use the respective index of a char to store 
            # the number of times it appeared in the current string
            for char in s:
                count[ord(char) - ord("a")] += 1
                # ord(char) - ord("a") calculates the "respective" index 
                # value of a char in the list <count>
            result[tuple(count)].append(s) 
            # Note: a LIST cannot be used as a key in a dict
            # Change the count list to tuple type (non-mutable)
        
        return list(result.values())

        
        