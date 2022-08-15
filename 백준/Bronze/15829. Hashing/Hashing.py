def alphabetNum(x):
    return ord(x)-96

N = int(input())
M = list(map(alphabetNum, input()))

sum = 0
for i in range(N):
    sum += M[i]*(31**i)
print(sum % 1234567891)