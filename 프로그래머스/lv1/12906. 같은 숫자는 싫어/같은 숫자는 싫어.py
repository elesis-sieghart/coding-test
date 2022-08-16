# 작성 코드 (95MB, 400ms)
def solution(arr):
    arr = list(map(str, arr))

    result = ''
    for i in range(len(arr)):
        if i==0: 
            result += arr[i]
        else: 
            result += ((lambda x, y: y if x!=y else '')(arr[i-1], arr[i]))

    return list(map(int, result)) 

# 다른 풀이 (29MB, 40ms)
def solution(arr):
    answer = []
    j = -1
    for i in arr:
        if i != j:
            j = i
            answer.append(i)

    return answer

# 아이고 간단한걸... 이렇게 돌아가기도 하는구나...
