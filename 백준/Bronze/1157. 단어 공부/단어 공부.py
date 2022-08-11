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

위 코드와 아래 코드의 결과는 같다.

c = []
for i in range(65, 91):
    c.append(s.count(chr(i)))
'''
