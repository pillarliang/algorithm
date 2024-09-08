"""recursion"""

# def count_construct(target: str, word_bank: list):
#     if target == '':
#         return True
#     total_count = 0
#     for word in word_bank:
#         if target.find(word) == 0:
#             count = count_construct(target[len(word):], word_bank)
#             total_count += count

#     return total_count
"""memoization"""

# def count_construct(target: str, word_bank: list, memo={}):
#     if target in memo:
#         return memo[target]

#     if target == '':
#         return 1
#     total_count = 0
#     for word in word_bank:
#         if target.find(word) == 0:
#             count = count_construct(target[len(word):], word_bank)
#             total_count += count

#     memo[target] = total_count
#     return total_count


class Solution():
    def count_construct(self, target: str, word_bank: list, memo={}):
        if target in memo:
            return memo[target]

        if target == '':
            return 1

        total_count = 0
        for word in word_bank:
            if target.find(word) == 0:
                count = self.count_construct(target[len(word):], word_bank,
                                             memo)
                total_count += count

        memo[target] = total_count
        return memo[target]


print(Solution().count_construct('purple',
                                 ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(Solution().count_construct("abcdef",
                                 ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(Solution().count_construct(
    "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(Solution().count_construct(
    "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(Solution().count_construct("eeeeeeeeeeeeeeeeeeeef",
                                 ['e'
                                  'ee'
                                  'eee'
                                  'eeee'
                                  'eeeee'
                                  'eeeeee']))
# 0
