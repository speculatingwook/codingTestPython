def data_input():
    M, N = map(int, input().split())
    cookies = list(map(int, input().split()))

    return M, N, cookies


def check_valid(cookies, target, target_people_count):
    people_count = 0

    if target == 0:
        return False

    for cookie in cookies:
        people_count += (cookie // target)

    if people_count >= target_people_count:
        return True
    else:
        return False


def solution():
    M, N, cookies = data_input()

    left, right = 0, int(10e9) + 1

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if check_valid(cookies, mid, M):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(solution())
