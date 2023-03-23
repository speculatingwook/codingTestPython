# def data_input():
#     N = int(input())
#     return N
#
#
# def solution():
#     N = data_input()
#     line = 1
#     num1, num2 = 0, 0
#     while N > line:
#
#         N -= line
#         line += 1
#
#         if line % 2 == 0:
#             num1 = N
#             num2 = line - N + 1
#         elif line % 2 == 1:
#             num1 = line - N + 1
#             num2 = N
#     print(num1, '/', num2, sep="")
#
#
# solution()
X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')
