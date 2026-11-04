class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        map_sp = {} # dog -> a
        map_ps = {} # a -> dog

        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            map_ps[pattern[i]] = map_ps.get(pattern[i], " ")
            if map_ps[pattern[i]] == " ":
                map_ps[pattern[i]] = words[i]
            else:
                if map_ps[pattern[i]] != words[i]:
                    return False
            
            map_sp[words[i]] = map_sp.get(words[i], " ")
            if map_sp[words[i]] == " ":
                map_sp[words[i]] = pattern[i]
            else:
                if map_sp[words[i]] != pattern[i]:
                    return False
        return True
        