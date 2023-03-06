
def data_input():
    M = int(input())
    M_list = list(map(int, input().split(" ")))
    M_list.sort()

    N = int(input())
    N_list = list(map(int, input().split(" ")))

    return M, N, M_list, N_list


def binary_search(list, target):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return 1
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


def solution():
    M, N, M_list, N_list = data_input()

    for element in N_list:
        print(binary_search(M_list, element), end=" ")


solution()