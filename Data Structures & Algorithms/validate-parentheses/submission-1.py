class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(':')', '{':'}','[':']'}
        stack = []
        for ch in s:
            if ch in mp:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mp[top]!=ch:
                    return False
        return len(stack)==0