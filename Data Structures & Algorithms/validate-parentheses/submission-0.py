class Solution:
    def isValid(self, s: str) -> bool:
        h = {']':'[','}':'{',')':'('}
        stack = []
        for c in s:
            if c not in h:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    pop_element = stack.pop()
                    if pop_element != h[c]:
                        return False
        return not stack
