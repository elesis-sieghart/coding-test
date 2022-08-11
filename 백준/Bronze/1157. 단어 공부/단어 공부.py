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
# 리스트 내포
c = [s.count(chr(i)) for i in range(65, 91)]
위 코드와 아래 코드의 결과값은 같다.

c = []
for i in range(65, 91):
    c.append(s.count(chr(i)))
https://wikidocs.net/22#for-range_1:~:text=%3E%3E%3E%20result%20%3D%20%5Bnum%20*%203%20for%20num%20in%20a%5D

# 아스키코드 함수들
ord(): str -> ascii (A->65)
chr(): ascii -> str (65->A)

# find, index
둘 다 (찾을 문자)가 처음 위치한 자리의 값 반환
'변수.find(찾을 문자)'
'변수.index(찾을 문자)'

문자를 찾는 시작점과 종료점을 지정 가능
'변수.find(찾을 문자, startIndex, endIndex)'
'변수.index(찾을 문자, startIndex, endIndex)'

find: 없는 경우 (return: -1)
index: 없는 경우 (ValueError)
사용가능한 자료형 차이는 아래 링크 참조
https://ooyoung.tistory.com/78

# count
문자열 안에서 찾고 싶은 문자의 개수 반환
'변수.count(찾을 문자)'
사용가능한 자료형 차이는 아래 링크 참조
https://ooyoung.tistory.com/76
'''
