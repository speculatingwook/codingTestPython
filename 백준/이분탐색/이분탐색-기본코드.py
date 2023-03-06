def binary_search(list, target):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


# 이 함수는 리스트와 찾으려는 값을 인자로 받아서, 찾으려는 값이 리스트에 있는 경우 해당 값의 인덱스를 반환하고, 없는 경우 None을 반환합니다.
#
# 이 함수의 동작은 다음과 같습니다.
#
#  1.리스트를 정렬합니다.
#  2.시작점(start)과 끝점(end)을 지정합니다. 일반적으로 start=0, end=len(list)-1로 초기화합니다.
#  3.시작점(start)이 끝점(end)보다 작거나 같은 동안 반복합니다.
#  4.중간점(mid)을 계산합니다. mid = (start+end) // 2로 계산합니다.
#  5.중간점의 값을 가져옵니다. value = list[mid]로 가져옵니다.
#  6.찾으려는 값(target)과 중간점의 값을 비교합니다.
#    1.target == value인 경우, 탐색을 종료하고 중간점을 반환합니다.
#    2.target < value인 경우, 끝점을 중간점-1로 변경합니다. (왼쪽 부분 리스트에서 탐색합니다.)
#    3.target > value인 경우, 시작점을 중간점+1로 변경합니다. (오른쪽 부분 리스트에서 탐색합니다.)
#  7.3~6 과정을 반복합니다. 시작점과 끝점이 같아질 때까지 반복합니다. 탐색을 종료하면 원하는 값을 찾지 못한 경우 None을 반환합니다.
#
# 이 함수를 사용하면 다음과 같이 이분탐색을 수행할 수 있습니다.

list = [1, 3, 5, 7, 9]
target = 5
result = binary_search(list, target)

if result is not None:
    print("Target found at index", result)
else:
    print("Target not found")

# 위 코드는 list에서 target을 찾는 이분탐색을 수행합니다. 리스트에 target이 있으면 해당 값의 인덱스가 출력되고, 없으면 "Target not found"가 출력됩니다.
