def data_input():
    N = int(input())

    return N


def solution():
    N = data_input()
    result_1, result_2 = dp_func(1, 0, 1, N)
    print(result_1, result_2)


def dp_func(a_element, b_element, N, E):
    result_a = b_element
    result_b = a_element + b_element
    if N == E:
        return result_a, result_b

    return dp_func(result_a, result_b, N + 1, E)


solution()

# 동훈이의 풀이
# import sys
#
# input = sys.stdin.readline
#
#
# def solution(K: int):
#     d = [[0, 0] for _ in range(45 + 1)]  # 0: A count, 1: B count
#     d[1] = [0, 1]
#
#     for i in range(2, K + 1):
#         d[i] = [d[i - 1][1], d[i - 1][0] + d[i - 1][1]]
#
#     print(d[K][0], d[K][1])
#
#
# K = int(input())
# solution(K)
