from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        l = list(s)
        res = ""
        str_s = ""
        num = ""
        while len(l) > 0:
            item = l.pop()
            if len(l) == 0:
                res = int(item) * str_s + res
                break
            if not item.isdigit() and num:
                num = int(num)
                str_s = num * str_s
                res = str_s + res
                num = ""
            if item == "]":
                str_s = ""
            elif item == "[":
                pass
            elif item.isdigit():
                num = item + num
            else:
                str_s = item + str_s
        return res


s = "3[a2[c]]"
print(Solution().decodeString(s))
