#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize hash table
        hash_table_size = 26
        hash_table = [0] * hash_table_size
        hash_func = lambda key: ord(key) - ord('a')

        # establish hash table
        for i in s:
            hash_table[hash_func(i)] += 1

        for i in t:
            hash_table[hash_func(i)] -= 1

        for i in hash_table:
            if i != 0:
                return False
        return True


s = ""
t = "car"
print(Solution().isAnagram(s, t))

# @lc code=end
