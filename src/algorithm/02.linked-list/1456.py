class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        res = 0

        for i in range(k):
            if s[i] in vowels:
                res += 1
        cur = res

        for i in range(len(s) - k):
            # 临界情况总是想很久qaq
            if s[i] in vowels:
                cur -= 1
            if s[i + k] in vowels:
                cur += 1
            res = max(cur, res)

        return res


s = "aeiou"
k = 2
print(Solution().maxVowels(s, k))
