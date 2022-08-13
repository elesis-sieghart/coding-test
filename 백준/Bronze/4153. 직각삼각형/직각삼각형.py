import sys

while True:
    val = list(map(int, sys.stdin.readline().strip().split()))

    if len(val)==3 and val[0]==0 and val[1]==0 and val[2]==0: break
    maxNum = max(val)
    val.remove(maxNum)
    print('right') if val[0]**2 + val[1]**2 == maxNum**2 else print('wrong')
    
# 다른 풀이
while True :
    nums = list(map(int, input().split()))
    
    if sum(nums) == 0:
        break  # 세 수가 0이면 break
        
    max_num = max(nums)
    nums.remove(max_num)  # 빗변의 길이는 직각삼각형 세변의 길이중 가장 길다.
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')
        
# del 예약어 : 인덱스로 삭제
# remove( ) 함수 : 값으로 삭제 (첫번째 값만 삭제)
'''
del arr[인덱스]
del arr[3:]

arr.remove('a')

https://ooyoung.tistory.com/49
'''

# 파이썬 예약어 종류: del, if, for, or, and
