def data_input():
    return list(map(int, input().split(" ")))


def solution():
    data = data_input()
    while True:
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                print(" ".join(map(str, data)))
        if data == [1, 2, 3, 4, 5]:
            break


solution()