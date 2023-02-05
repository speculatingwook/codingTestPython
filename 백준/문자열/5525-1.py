def P(n):
    if(n==1):
        return "IOI"
    str = "OI"
    return P(n-1)+str



n = int(input())
inputStringLength = int(input())
inputString = input()


count = 0
for i in range(0, inputStringLength-len(P(n))+1):
    if(inputString[i:i+len(P(n))] == P(n)):
        count+=1

print(count)


