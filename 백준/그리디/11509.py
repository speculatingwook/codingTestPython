# 요구사항
# 연속된


def solution():
    number = int(input())
    height = list(map(int, input().split(" ")))
    # arrow_count의 인덱스가 화살의 높이, 인덱스에 해당하는 값이 박힌 화실의 개수를 의미한다.
    arrow_count = [0] * (max(height) + 1)

    # i: 화살의 높이

    for i in height:
        # 해당 인덱스(높이)에 화살이 박혀있을 때
        if arrow_count[i] > 0:
            # 화살을 뽑는다.
            arrow_count[i] -= 1
            # 화살의 높이를 1 내린 상태에 화살을 박는다.
            arrow_count[i - 1] += 1

        # 화살이 박혀있지 않을 때
        else:
            # 화살을 추가하고, 높이를 1 내린 상태에 박아둔다.
            arrow_count[i - 1] += 1

    # 총 박혀있는 화살의 개수 -> 최소한으로 쏜 화살의 개수
    return sum(arrow_count)


print(solution())
