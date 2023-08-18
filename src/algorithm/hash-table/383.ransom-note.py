#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = dict()
        for i in magazine:
            magazine_dict[i] = magazine_dict.get(i, 0) + 1

        for i in ransomNote:
            if i in magazine_dict and magazine_dict[i]:
                magazine_dict[i] = magazine_dict.get(i) - 1
            else:
                return False

        return True


# @lc code=end
# ransomNote = "a"
# magazine = "b"

# ransomNote = "aa"
# magazine = "ab"

ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
