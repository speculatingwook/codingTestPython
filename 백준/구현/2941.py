croatia_alphabet_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


def data_input():
    input_string = str(input())
    return input_string


def solution():
    word = data_input()
    for croatia in croatia_alphabet_list:
        word = word.replace(croatia, '*')  # input 변수와 동일한 이름의 변수
    return len(word)


print(solution())