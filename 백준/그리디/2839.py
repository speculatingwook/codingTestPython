def solution(weight):
    bag = weight // 5
    remainder = weight % 5
    while remainder != 0:
        if bag < 0:
            return -1
        elif remainder % 3 == 0:
            bag = bag + remainder // 3
            return bag
        elif remainder % 3 != 0:
            bag -= 1
            remainder += 5
    return bag


number = int(input())
print(solution(number))
