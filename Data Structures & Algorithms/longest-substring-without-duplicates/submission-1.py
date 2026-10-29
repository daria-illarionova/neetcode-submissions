class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = set()
        
        start_ptr = 0

        max_len = 0
        
        for end_ptr in range(len(s)):

            # case - encounter a duplicate char: update the window & set
            # while loop executes until left/start pointer moved up such that the current substring no longer has duplicates
            while s[end_ptr] in unique:
                unique.remove(s[start_ptr])
                start_ptr += 1
            unique.add(s[end_ptr])

            # at this point know for sure the substring does not contain duplicates
            # compare current substring length to max_len counter
            # compute substring length = end_ptr - start_ptr + 1
            max_len = max(max_len, end_ptr - start_ptr + 1)

        return max_len


        