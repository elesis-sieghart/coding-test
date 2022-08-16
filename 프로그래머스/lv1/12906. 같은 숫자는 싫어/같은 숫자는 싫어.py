def solution(arr):
    arr = list(map(str, arr))
    
    result = ''
    for i in range(len(arr)):
        if i==0: 
            result += arr[i]
        else: 
            result += ((lambda x, y: y if x!=y else '')(arr[i-1], arr[i]))
    
    return list(map(int, result))