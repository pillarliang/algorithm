from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        solutions = [False]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    initial_state = {
                        "path": set(),
                        "current_position": (r, c),
                        "word_index": 0,
                    }
                    self.search(board, word, initial_state, solutions)
                    if solutions[0]:
                        return True
        return False

    def search(self, board, word, state, solutions):
        if self.is_valid_state(word, state):
            solutions[0] = True
            return

        for candidate in self.get_candidates(board, word, state):
            r, c, word_index = candidate
            state["path"].add((r, c))
            state["current_position"] = (r, c)
            state["word_index"] = word_index

            self.search(board, word, state, solutions)

            state["path"].remove((r, c))
            state["current_position"] = (r, c)
            state["word_index"] = word_index - 1

    def is_valid_state(self, word, state):
        return state["word_index"] == len(word)

    def get_candidates(self, board, word, state):
        candidates = []
        r, c = state["current_position"]
        word_index = state["word_index"]

        if board[r][c] != word[word_index]:
            return candidates

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        next_index = word_index + 1

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (
                0 <= new_r < len(board)
                and 0 <= new_c < len(board[0])
                and (new_r, new_c) not in state["path"]
            ):
                candidates.append((new_r, new_c, next_index))

        return candidates


# 示例用法
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution().exist(board, word))  # 输出: True
