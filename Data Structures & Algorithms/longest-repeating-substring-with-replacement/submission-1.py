import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = dict.fromkeys(string.ascii_uppercase, 0)
        # {'A': 0, 'B': 0, 'C': 0, ..., 'Z': 0}

        max_len = 0

        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            # number of replacements = len(substring) - max freq. char
            # max freq. char = max(freq, key = freq.get)

            while (len(s[l:r+1]) - freq[max(freq, key = freq.get)]) > k:
                freq[s[l]] -= 1
                l += 1
            
            # at this point, certain substring is valid
            max_len = max(max_len, len(s[l:r+1]))
            # r incrementend automatically at the end of curr FOR itteration
        
        return max_len
        



        