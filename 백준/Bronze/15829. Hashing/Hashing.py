# 해시 함수의 정의에서 유한한 범위의 출력을 가져야 한다고 했으니까 적당히 큰 수 M으로 나눠주자.
# 문제에서 M을 1234567891로 주었다.

def alphabetNum(x):
    return ord(x)-96

N = int(input())
M = list(map(alphabetNum, input()))

sum = 0
for i in range(N):
    sum += M[i]*(31**i)
print(sum % 1234567891)
