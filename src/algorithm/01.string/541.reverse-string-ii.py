#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#


# @lc code=start
class Solution:

    def reverseStr_old(self, s: str, k: int) -> str:
        count = 0
        while count < len(s):
            count2 = count + k
            s = s[:count] + s[count:count2][::-1] + s[count2:]
            count = count2 + k
        return s

    def reverseStr(self, s: str, k: int) -> str:
        # 将字符串转化为列表，这样我们可以就地修改字符
        list_s = list(s)

        for i in range(0, len(s), 2 * k):
            # 反转前 k 个字符
            list_s[i : i + k] = reversed(list_s[i : i + k])

        return "".join(list_s)


# @lc code=end
# s = "abcdefg"
# k = 2

s = "abcd"
k = 2
print(Solution().reverseStr(s, k))
