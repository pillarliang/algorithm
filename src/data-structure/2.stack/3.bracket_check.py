def bracket_check(str):
    stack = []
    for item in str:
        if item == '(':
            stack.append(')')
        elif item == '[':
            stack.append(']')
        elif item == '{':
            stack.append('}')
        elif not stack or stack[-1] != item:
            return False
        else:
            stack.pop()
    return True if not stack else False


print(bracket_check("()[]{}"))
print(bracket_check("(]"))
