def data_input():
    number = int(input())
    total_data = []

    for _ in range(number):
        scale = list(map(int, input().split(" ")))
        total_data.append(scale)

    return number, total_data


def calc_scale(total_data: list[list[int]], index: int) -> int:
    count = 0
    for scale in total_data:
        if scale == total_data[index]:
            pass
        elif total_data[index][0] < scale[0] and total_data[index][1] < scale[1]:
            count += 1
    return count + 1


def solution():
    number, total_data = data_input()

    for i in range(number):
        print(calc_scale(total_data, i), end=' ')


solution()