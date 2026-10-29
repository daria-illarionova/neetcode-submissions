class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create hash table for the character freq in s and t
        frequency_s = {}
        frequency_t = {}

        # populate hash table for s and t
        for char in s:
            if char not in frequency_s:
                frequency_s[char] = 1
            else:
                frequency_s[char] += 1
        
        for char in t:
            if char not in frequency_t:
                frequency_t[char] = 1
            else:
                frequency_t[char] += 1

        # uneven number of chars in string s & t indicate theyre not valid anagrams
        # length check allows us to only use one for loop for both frequency dictionaries.
        if len(frequency_s) != len(frequency_t):
            return False

        # compare hash table for s & t
        for char_s in frequency_s:
            # freq_s = frequency_s[char_s]
            if char_s not in frequency_t or frequency_t[char_s] != frequency_s[char_s]:
                return False
        return True

        