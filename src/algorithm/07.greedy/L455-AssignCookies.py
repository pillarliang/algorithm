from typing import List


# Different from the "code caprice" idea
class Solution:
    def findContentChildren_v1(self, g: List[int], s: List[int]) -> int:
        """
        Avoid waste: Distribute small cookies to child whenever possible
        """
        g.sort()
        s.sort()
        res = 0
        i = 0
        for child in g:
            while i < len(s):
                if s[i] >= child:
                    res += 1
                    i += 1
                    break
                else:
                    i += 1
        return res

    def findContentChildren_v2(self, g: List[int], s: List[int]) -> int:
        """
        Satisfying desires: Distribute big cookies to child whenever possible
        """
        g.sort()
        s.sort()
        res = 0
        i = len(s) - 1
        for child in g[::-1]:
            if i >= 0 and s[i] >= child:
                res += 1
                i -= 1
        return res


so = Solution()
g = [1, 2, 3]
s = [1, 1]

# g = [10, 9, 8, 7]
# s = [5, 6, 7, 8]

print(so.findContentChildren_v1(g, s))
print(so.findContentChildren_v2(g, s))
