val = input().upper()

length = len(val)
lst = [0]*26

for v in val:
    lst[ord(v)-65] += 1

if(lst.count(max(lst))>1):
    print('?')
else:
    i = lst.index(max(lst))
    print(chr(i+65))
    
# 다른 풀이 (32796KB, 88ms)
s = input().upper();
c = [s.count(chr(i)) for i in range(65, 91)]
m = max(c)
if(c.count(m) == 1):
    print(chr(c.index(m)+65))
else:
    print('?')
    
'''
c = [s.count(chr(i)) for i in range(65, 91)]

위 코드(리스트 내포)와 아래 코드의 결과는 같다. 
https://wikidocs.net/22#for-range_1:~:text=%3E%3E%3E%20result%20%3D%20%5Bnum%20*%203%20for%20num%20in%20a%5D

c = []
for i in range(65, 91):
    c.append(s.count(chr(i)))
'''
