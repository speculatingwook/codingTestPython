def backtrack(n, k, s):
    if n == k:
        print(result)
    else:
        for i in range(s, len(numbers)):
            result[n] = numbers[i]
            backtrack(n+1, k, i+1)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [0, 0, 0, 0]
backtrack(0, 4, 0)