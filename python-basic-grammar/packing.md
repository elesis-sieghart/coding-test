# packing, unpacking
묶고 푸는 것

## 1. 튜플
```py
# 튜플 패킹 => 소괄호가 없어도 된다.
square = (20, 20) # (20, 40)
square = 20, 20   # (20, 40)
```
```py
# 튜플 언패킹
width, height = square # 20 20

# 튜플 언패킹시 리스트로 묶을 수도 있다. (리스트로 묶을때 *를 사용한다.)
num = 1, 2, 3, 4, 5
n1, n2, *others = num  # [3, 4, 5]

# 리스트 언패킹
num = [1, 2, 3]
n1, n2, n3 = num
```
## 2. 함수  
함수의 호출, 반환에서 패킹/언패킹이 가능하다.
 ```py
 def makeTuple():
  return 1, 2, 3
 
 makeTuple() # (1, 2, 3)
 n1, *other = makeTuple() # [2, 3]
 ```

## 3. 중첩 튜플
```py
num = ((1, 2), 3)
(n1, n2), n3 = num
```

## 언패킹 관례
```py
# 안쓰는 값은 관례적으로 _변수에 담는다.
num = ((1, 2), 3)
(n1, _), _ = num
```
## 루프에서의 언패킹
```py
data = [(1, 1), (2, 2)]

for width, height in data:
  print(width, height)
```
