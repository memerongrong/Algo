for tc in range(int(input())):
    brackets = list(input())
    stack = []
    VPS = "YES"

    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')' and len(stack) >= 1:
            stack.pop()
        else:
            VPS = "NO"
            break

    if len(stack) >= 1:
        VPS = "NO"

    print(VPS)