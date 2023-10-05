def all_construct(target: str, word_bank: list):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for index, item in enumerate(table):
        for word in word_bank:
            if target[index:(index + len(word))] == word:
                new_combinations = [sub_array + [word] for sub_array in item]
                table[index + len(word)] += new_combinations

    return table[len(target)]


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
