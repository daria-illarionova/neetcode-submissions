from collections import Counter
''' Counter is a specialized dictionary subclass from the built-in collections module. It is designed specifically to count the frequencies of hashable objects efficiently without needing manual loops '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using a dictionary
        # Keep track of character and corresponding character count for both strings
        
        freq_s = Counter(s)
        freq_t = Counter(t)

        if freq_s == freq_t:
            return True
        return False