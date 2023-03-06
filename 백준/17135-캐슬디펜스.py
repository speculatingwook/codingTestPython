# 요구사항 명세서
#
# - 나올 수 있는 경우들 중에서 최댓값 반환
# - 궁수의 위치 결정(조합)
# - 리스트에서 1이 있다면 궁수와의 거리 계산
# - 만약 최대 거리 이내라면 1 삭제, 결과 추가, 모든 궁수가 쏜 후, 리스트 마지막줄 삭제, 리스트 윗줄 0 append -
# - 리스트 내에서 1이 없다면, 결과 반환 -
from itertools import combinations


def distance(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def step_calc(field):
    field.pop()
    field.insert(0, [0] * field[1].length)
    return field


def check_field_done(field):
    for line in field:
        for one in line:
            if one == 1:
                return False
    return True


def archer_location(N):
    combinations(N, 3)


def data_input():
    N, M, D = map(int, input().split(" "))
    field = []
    for i in range(N):
        line = list(input())
        field.append(line)
    return N, M, D, field


def solution():
    N, M, D, field = data_input()
