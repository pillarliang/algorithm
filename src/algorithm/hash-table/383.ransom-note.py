#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
from collections import Counter


class Solution1:
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


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)


class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all((ransomNote.count(s) <= magazine.count(s)
                    for s in set(ransomNote)))


# ransomNote = "a"
# magazine = "b"

# ransomNote = "aa"
# magazine = "ab"

ransomNote = "aa"
magazine = "aab"
print(Solution3().canConstruct(ransomNote, magazine))
