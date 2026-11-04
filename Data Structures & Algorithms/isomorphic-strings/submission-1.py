class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create the dictionary with " " as the default value
        map_t = dict.fromkeys(t, " ")
        map_s = dict.fromkeys(s, " ")
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if map_t[t[i]] != " ":
                if map_t[t[i]] != s[i]:
                    return False
            else:
                map_t[t[i]] = s[i]
                
            if map_s[s[i]] != " ":
                if map_s[s[i]] != t[i]:
                    return False
            else:
                map_s[s[i]] = t[i]
        return True
        
        # Returns True if NO value is " ", returns False if any value is " "
        # return all(value != " " for value in map_t.values()) 
        