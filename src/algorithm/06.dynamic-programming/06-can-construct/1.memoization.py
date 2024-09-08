"""recursion"""

# def can_construct(target: str, word_bank: list):
#     if target == '':
#         return True
#     for word in word_bank:
#         if target.find(word) == 0:
#             if can_construct(target[len(word):], word_bank) is True:
#                 return True

#     return False
"""memoization"""

# def can_construct(target: str, word_bank: list, memo={}):
#     if target in memo:
#         return memo[target]

#     if target == '':
#         return True
#     for word in word_bank:
#         if target.find(word) == 0:
#             if can_construct(target[len(word):], word_bank, memo) is True:
#                 memo[target] = True
#                 return True

#     memo[target] = False
#     return False


class Solution():
    def can_construct(self, target: str, word_bank: list, memo={}):
        if target in memo:
            return memo[target]

        if target == '':
            return True

        for item in word_bank:
            item_s_index = target.find(item)
            if item_s_index == 0:
                memo[target] = self.can_construct(target.replace(item, ''),
                                                  word_bank, memo)
                if memo[target]:
                    return memo[target]

        memo[target] = False
        return memo[target]


print(Solution().can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# true
print(Solution().can_construct("skateboard",
                               ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# False
print(Solution().can_construct("enterapotentpot",
                               ["a", "p", "ent", "enter", "ot", "o", "t"]))
# true
print(Solution().can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
]))
# false
