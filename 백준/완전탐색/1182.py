from itertools import combinations
from typing import List


def data_input() -> (int, int, List[int]):
    number, target_integer = map(int, input().split())
    number_list = list(map(int, input().split()))
    return number, target_integer, number_list


def solution():
    number, target_integer, number_list = data_input()
    count = 0
    for i in range(1, number + 1):
        comb_list = list(combinations(number_list, i))

        for element in comb_list:
            if sum(element) == target_integer:
                count += 1
    print(count)


solution()
