from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        next_can_placed = True

        for index, item in enumerate(flowerbed):
            if not n:
                return True

            if item == 1:
                next_can_placed = False
            elif item == 0 and next_can_placed:
                if index + 1 < len(flowerbed) and flowerbed[index + 1] == 1:
                    next_can_placed = True
                else:
                    next_can_placed = False
                    n -= 1
            elif item == 0:
                next_can_placed = True

        return False if n else True


# print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
# print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))  # False
print(Solution().canPlaceFlowers([0, 0, 1, 0, 0], 1))  # True
