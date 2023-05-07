def count_construct(target: str, word_bank: list):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for index, item in enumerate(table):
        if item != 0:
            for word in word_bank:
                if target[index:(index + len(word))] == word:
                    table[index + len(word)] += item

    return table[len(target)]


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(
    count_construct("skateboard",
                    ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(
    count_construct("enterapotentpot",
                    ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(
    count_construct("eeeeeeeeeeeeeeeeeeeef",
                    ['e'
                     'ee'
                     'eee'
                     'eeee'
                     'eeeee'
                     'eeeeee']))
# 0
