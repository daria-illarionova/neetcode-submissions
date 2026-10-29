class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Removes all non-alphanumeric characters using a list comprehension.
        # Then converts all uppercase characters in a string to lowercase.
        s = "".join(char for char in s if char.isalnum()).lower()
        
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True