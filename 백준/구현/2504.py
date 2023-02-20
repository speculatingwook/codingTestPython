def data_input():
    string = list(input())
    return string


def solution():
    bracket = data_input()
    stack = []
    answer = 0
    tmp = 1

    for i in range(len(bracket)):

        if bracket[i] == "(":
            stack.append(bracket[i])
            tmp *= 2

        elif bracket[i] == "[":
            stack.append(bracket[i])
            tmp *= 3

        elif bracket[i] == ")":
            if not stack or stack[-1] == "[":
                answer = 0
                break
            if bracket[i-1] == "(":
                answer += tmp
            stack.pop()
            tmp //= 2

        else:
            if not stack or stack[-1] == "(":
                answer = 0
                break
            if bracket[i-1] == "[":
                answer += tmp

            stack.pop()
            tmp //= 3

    if stack:
        return 0
    else:
        return answer


print(solution())

