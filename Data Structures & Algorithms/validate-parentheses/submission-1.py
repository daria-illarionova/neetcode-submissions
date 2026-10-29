class Solution:
    def isValid(self, s: str) -> bool:
        # Stack push .append()
        # Stack pop .pop()
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for x in s:
            if x in brackets.values():
                stack.append(x)
            else:
                # Stack of open brackets ended before closed brackets
                if len(stack) == 0:
                    return False
                else:
                    last_bracket = stack.pop()
                    if brackets[x] != last_bracket:
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False




        