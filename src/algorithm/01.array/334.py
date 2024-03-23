from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        mid = 1
        for idx, item in enumerate(chars):
            if idx == len(chars) - 1 or chars[idx + 1] != item:
                s += item
                s += str(mid)
                mid = 1
            else:
                mid += 1
        return list(s)


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
