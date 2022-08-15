N = int(input())
sum = 1
num = 1
while 1:
    if N <= sum: 
        print(num) 
        break
    sum += 6*num
    num += 1