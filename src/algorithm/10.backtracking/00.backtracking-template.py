def solve():
    solutions = []  # 存储所有有效解决方案的列表。
    state = set()  # current state
    search(state, solutions)  # 通过尝试所有可能的候选项来构建解决方案。
    return solutions


def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def is_valid_state(state):
    # check if it is a valid solution
    return True


def get_candidates(state):
    """生成当前状态下所有可能的候选项。"""
    # 获取下一个元素的合法state
    return []
