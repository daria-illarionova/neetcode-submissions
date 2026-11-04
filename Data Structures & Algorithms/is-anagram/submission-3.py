class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        Intuition: if len(s) != len(t) they cannot be anagrams 
        because one string contains more chars than the other 
        (aka different freq's).
        
        If the lengths are equal, then we only need to itterate through one 
        of the strings indices but are able to access the indices of both
        (using the same pointer) 
        => only require one for loop to populate both frequency array.
        
        """
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        return freq_s == freq_t

        