number = int(input())
inputStringLength = int(input())
inputString = input()


def solution():
    i, answer, count = 0, 0, 0
    while i < (inputStringLength - 1) :
        if inputString[i:i+3] == 'IOI':
            i+=2
            count+=1
            if count == number:
                answer +=1
                count -= 1
        else:
            i += 1
            count =0

    return answer

print(solution())


IOIOIOIOIOIOI