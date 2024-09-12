from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        solutions = [False]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    initial_state = {
                        "path": set(),  # 确保每个单元格只访问一次，避免循环和重复计算。
                        # 跟踪当前搜索的位置，以便在递归调用中进行正确的移动。
                        "current_position": (r, c),
                        "word_index": 0,  # 记录当前匹配到的单词字符索引，以便检查是否已经找到完整的单词。
                    }
                    self.search(board, word, initial_state, solutions)
                    if solutions[0]:
                        return True
        return False

    def search(self, board, word, state, solutions):
        if self.is_valid_state(word, state):
            solutions[0] = True
            return

        r, c = state["current_position"]
        word_index = state["word_index"]

        if board[r][c] != word[word_index]:
            return

        for candidate in self.get_candidates(board, word, state):
            new_r, new_c = candidate
            state["path"].add((new_r, new_c))
            state["current_position"] = (new_r, new_c)
            state["word_index"] = word_index + 1

            self.search(board, word, state, solutions)

            state["path"].remove((new_r, new_c))
            state["current_position"] = (r, c)
            state["word_index"] = word_index

    def is_valid_state(self, word, state):
        return state["word_index"] == len(word) - 1

    def get_candidates(self, board, word, state):
        candidates = []
        r, c = state["current_position"]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (
                0 <= new_r < len(board)
                and 0 <= new_c < len(board[0])
                and (new_r, new_c) not in state["path"]
            ):
                candidates.append((new_r, new_c))

        return candidates


# 示例用法
# board = [["a"]]
# word = "a"  # 输出: True

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"  # True

board = ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],)
word = "ABCB"  # False

print(Solution().exist(board, word))
