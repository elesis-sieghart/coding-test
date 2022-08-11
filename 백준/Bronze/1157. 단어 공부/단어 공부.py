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