#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

from collections import Counter, defaultdict


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


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict


s = "abcddce"
t = "abcddce"
print(Solution3().isAnagram(s, t))
