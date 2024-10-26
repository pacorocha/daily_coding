def balanced_brackets(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for c in s:
        print(stack)
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack or stack[-1] != brackets[c]:
                return 'NO'
            stack.pop()

    return 'YES' if not stack else 'NO'

if __name__ == '__main__':
    s = '{(([])[])[]}'

    print(balanced_brackets(s))

