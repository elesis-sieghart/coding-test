N = int(input())
sum = 1
num = 1
while 1:
    if N <= sum: 
        print(num) 
        break
    sum += 6*num
    num += 1
    
'''
1 (+6*0) => 1칸(1)
1 (+6*1) => 2칸(2~7)
7 (+6*2) => 3칸(8~19)
19(+6*3) => 4칸(20~37) 
37(+6*4) => 5칸(38~61)
61(+6*5) => 6칸(62~)
...
'''

# 다른 풀이 (29056KB 56ms)
n = int(input())
i = 1
while(n>1):
    n -= 6*i
    i += 1
print(i)
