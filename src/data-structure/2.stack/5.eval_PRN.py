def eval_RPN(tokens: list[str]) -> int:
    """Evaluate Reverse Polish Notation"""
    add = lambda a, b: a + b
    sub = lambda a, b: a - b
    mul = lambda a, b: a * b
    div = lambda a, b: a / b
    op_map = {'+': add, '-': sub, '*': mul, '/': div}

    stack = []
    for token in tokens:
        if token not in op_map:
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(op_map[token](a, b))
    return stack.pop()


tokens = ["2", "1", "+", "3", "*"]
print(eval_RPN(tokens))
