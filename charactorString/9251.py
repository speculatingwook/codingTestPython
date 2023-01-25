def solution(fWord, sWord):
    f_length , s_length = len(fWord), len(sWord)
    LCS = [[0]*(s_length+1)]*(f_length+1)

    for i in range(1, f_length+1):
        for j in range(1, s_length+1):
            if(fWord[i-1] == sWord[j-1]):
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j]= max(LCS[i-1][j], LCS[i][j-1])
    return LCS[-1][-1]

firstWord = input()
secondWord = input()

print(solution(firstWord, secondWord))
