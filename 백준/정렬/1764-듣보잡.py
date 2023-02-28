def data_input():
    N, M = map(int, input().split())

    a = set()
    for i in range(N):
        a.add(input())

    b = set()
    for i in range(M):
        b.add(input())

    return a, b


def solution():
    a, b = data_input()
    answers = sorted(list(a & b))

    print(len(answers))
    for answer in answers:
        print(answer)

solution()