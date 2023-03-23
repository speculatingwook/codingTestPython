def data_input():
    N = int(input())
    return N


def solution():
    N = data_input()
    for i in range(1, N+1):
        print(" "* (N-i) + "*"*(2*i-1))
    for i in range(1, N):
        print(" "*i+ "*"*(2*(N-i)-1))

solution()