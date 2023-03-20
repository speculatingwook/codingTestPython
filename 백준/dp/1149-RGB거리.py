def data_input():
    N = int(input())
    color_options = []
    for i in range(N):
        prices = list(map(int, input().split()))
        color_options.append(prices)
    return N, color_options


def solution():
    N, color_options = data_input()

    for i in range(1, N):
        color_options[i][0] = min(color_options[i - 1][1], color_options[i - 1][2]) + color_options[i][0]
        color_options[i][1] = min(color_options[i - 1][0], color_options[i - 1][2]) + color_options[i][1]
        color_options[i][2] = min(color_options[i - 1][0], color_options[i - 1][1]) + color_options[i][2]
    return min(color_options[N - 1][0], color_options[N - 1][1], color_options[N - 1][2])


print(solution())
