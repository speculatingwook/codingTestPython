def input_data():
    N = int(input())

    positive = []
    negative = []
    sum_max = 0

    for _ in range(N):
        a = int(input())
        if a > 1:
            positive.append(a)
        elif a == 1:
            sum_max += 1
        else:
            negative.append(a)

    positive.sort(reverse=True)
    negative.sort()

    return N, positive, negative, sum_max


def solution():
    N, positive, negative, sum_max = input_data()

    # 양수 리스트 더해주기
    if len(positive) % 2 == 0:
        for i in range(0, len(positive), 2):
            sum_max += positive[i] * positive[i + 1]
    else:
        for i in range(0, len(positive) - 1, 2):
            sum_max += positive[i] * positive[i + 1]
        sum_max += positive[len(positive) - 1]

    # 음수 더해주기
    if len(negative) % 2 == 0:
        for i in range(0, len(negative), 2):
            sum_max += negative[i] * negative[i + 1]
    else:
        for i in range(0, len(negative) - 1, 2):
            sum_max += negative[i] * negative[i + 1]
        sum_max += negative[len(negative) - 1]

    print(sum_max)


solution()
