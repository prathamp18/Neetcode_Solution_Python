class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p = ''.join([char for char in s if char.isalnum()])
        n = len(p)
        l = 0
        r = n-1
        while (l<=r):
            if(p[l]!=p[r]):
                return False
            l+=1
            r-=1
        return True