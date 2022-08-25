# Compound Data Types
여러개의 값을 저장할 수 있는 데이터 타입  
모든 복합자료형은 어떠한 자료형도 담을 수 있다.

# Sequence Types
시퀀스형이란?
- 0개 이상의 객체를 배열 형태로 참조하는 자료형
- 따라서 담고 있는 각 객체는 순서를 갖고있다.

가장 많이사용하는 시퀀스형
- 문자열(str)
- 리스트(list)
- 튜플(tuple)

기타 시퀀스형
- bytearray
- bytes
- collections.namedtuple

## 리스트형(List Type)
가변자료형(mutable)
- 생성 후 내용 변경이 가능하다. 담은 객체의 삭제, 변경, 삽입이 가능하다.
- 순서를 가지는 0개 이상의 객체를 ```참조```하는 시퀀스형이다.

### 리스트 생성
1. **[]** (대괄호)
2. **list()** 생성자(클래스)
3. 리스트 축약 (list comprehension) ```[표현식 for 변수 in 순회형 <if 불린-표현식>]```
```py
arr = [1, 2, 3] # [1, 2, 3]

# list()의 전달인자로 순회형만 올 수 있다.
arr = list('123') # ['1', '2', '3']
arr = list(123)   # TypeError: 'int' object is not iterable

arr = [_ for _ in range(3)] # [0, 1, 2]
```
- **순회형(iterable)** 이란 담고 있는 객체들에 하나씩 순서대로 접근할 수 있는 자료형 (문자열, 리스트, 튜플, 딕셔너리, 세트)
- **len()** 함수는 순회형 객체의 길이를 반환한다.

### 리스트 관련 연산자
결합 연산자 : **+**  
반복 결합 연산자 : __*__  
확장 연산자 : **+=**  

분할 연산자 : **[:]**  
삭제 연산자 : **del**  
멤버십 연산자 : **in/not in**  
```py
# 결합, 반복 결합 연산자
[1, 2] + [3, 4] # [1, 2, 3, 4]
[0] * 5         # [0, 0, 0, 0, 0]
[1, 2] * 2      # [1, 2, 1, 2]

# 확장 연산자
lst = ['Hello']
lst += ['World'] # ['Hello', 'World']
lst += !!!       # ['Hello', World', '!', '!', '!']

lst += 1   # TypeError: 'int' object is not iterable
lst += [1] # ['Hello', World', '!', '!', '!', 1]
```
```py
s = ['a', 'b', ['c', 'd'], 'e']

# 분할 연산자
s[:]          # 전체 추출, s[0:len(s)]와 같다.
s[0:2] = [1, 2] # 일부 교체 [1, 2, ['c', 'd'], 'e']
s[:] = []     # 리스트 모든 객체를 빈 리스트로 교체

# 삭제 연산자
  # del은 객체의 참조를 삭제하는 연산자이다.
  # 따라서 파이썬의 모든 자료형에서 객체 참조를 삭제하는 데 사용할 수 있다.
del s[2][1]   # ['a', 'b', ['c'], 'e']
del s[2:4]    # ['a', 'b']
del s[:]      # []

# 멤버십 연산자
  # 순회형 값 안에 객체 존재 여부를 T/F로 알려준다.
  # 순회형에 적용할 수 있기에 문자열에 일부 문자가 포함되었는지 확인할 때에도 사용 가능하다.
'a' in s # True
'c' in s # False
'c' in s[2] # True

text = 'Hello World!'
'H' in text       # True
' World!' in text # True
```
### 리스트 관련 메소드
복사 메소드 : **copy()**  
추가 메소드 : **append(), extend(), insert()**  
삭제 메소드 : **pop(), remove()**  
질의 메소드 : **count(), index()**  
정렬 메소드 : **reverse(), sort()**  
```py
L = [1, 2, ['x', 'y']]

# 복사 메소드 : L.copy()
  # 얕은 복사(shallow copy) 반환
y = L.copy() # 리스트 x를 얕은 복사해 변수 y에 할당

# 추가 메소드 : L.append(x), L.extend(m), L.insert(i, x)
L.append(3) # [1, 2, ['x', 'y'], 3]
L.append(['z']) # [1, 2, ['x', 'y'], 3, ['z']]

L.extend(['z']) # [1, 2, ['x', 'y'], 'z']
L += ['z']      # [1, 2, ['x', 'y'], 'z']

L.insert(2, 3) # [1, 2, 3, ['x', 'y']]

# 삭제 메소드


# 질의 메소드
# 정렬 메소드
```

## Tuple Type

# Mapping Types
## Dictionary Type

# Set Type
## set
