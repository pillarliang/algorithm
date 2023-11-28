def solve():
    solutions = []
    state = set()
    search(state, solutions)
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
    # 获取下一个元素的合法state
    return []
