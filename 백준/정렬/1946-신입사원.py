import sys

input = sys.stdin.readline


def test_case_number():
    return int(input())


def applier_list_data():
    N = int(input())
    data_list = []

    for i in range(N):
        x, y = map(int, input().split())
        data_list.append([x, y])

    data_list.sort()
    return data_list


def solution():
    T = test_case_number()

    for i in range(T):
        sorted_data_list = applier_list_data()

        # 서류시험 1등의 면접시험 순위를 넣는다.
        # 만약 다른 참여자들이 서류시험 1등의 면접시험보다 잘보면 무조건 붙는다.
        standard = sorted_data_list[0][1]
        index = 1
        for j in range(1, len(sorted_data_list)):
            if sorted_data_list[j][1] < standard:
                standard = sorted_data_list[j][1]
                index += 1
        print(index)


solution()
