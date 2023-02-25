from itertools import combinations


def data_input():
    number, M = map(int, input().split(" "))
    card = list(map(int, input().split(" ")))
    return number, M, card


def solution():
    number, M, card = data_input()
    sum_combi = list(combinations(card, 3))
    max_sum = 0
    for i in range(len(sum_combi)):
        if sum(sum_combi[i]) <= M:
            max_sum = max(max_sum, sum(sum_combi[i]))
    print(max_sum)

solution()