# def can_construct(target: str, word_bank: list) -> bool:
#     table = [False] * (len(target) + 1)
#     table[0] = True

#     for index, item in enumerate(table):
#         if item is True:
#             for word in word_bank:
#                 if target[index:index + len(word)] == word:
#                     table[index + len(word)] = True

#     return table[len(target)]


class Solution():
    def can_construct(self, target: str, word_bank: list) -> bool:
        table = [False] * (len(target) + 1)
        table[0] = True

        for index, item in enumerate(table):
            if item:
                for word in word_bank:
                    if target[index:index + len(word)] == word:
                        table[index + len(word)] = True

        return table[len(target)]


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
