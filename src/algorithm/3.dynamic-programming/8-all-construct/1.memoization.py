"""recursion"""

# def all_construct(target, work_bank):
#     if target == '':
#         return [[]]
#     result = []

#     for word in work_bank:
#         if target.find(word) == 0:
#             suffixWays = all_construct(target[len(word):], work_bank)
#             targetWays = []
#             for way in suffixWays:
#                 way.append(word)
#                 targetWays.append(way)
#             result += targetWays

#     return result
"""memoization"""


def all_construct(target, work_bank, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]
    result = []

    for word in work_bank:
        if target.find(word) == 0:
            suffixWays = all_construct(target[len(word):], work_bank, memo)
            targetWays = []
            for way in suffixWays:
                way.append(word)
                targetWays.append(way)
            result += targetWays

    memo[target] = result
    return result


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
# [ 'purp', 'le' ],
# [ 'p', 'ur', 'p', 'le' ]
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [ 'ab', 'cd', 'ef' ],
# [ 'ab', 'c', 'def' ],
# [ 'abc', 'def' ],
# [ 'abcd', 'ef' ]
print(
    all_construct("skateboard",
                  ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
print(
    all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz",
                  ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # []
