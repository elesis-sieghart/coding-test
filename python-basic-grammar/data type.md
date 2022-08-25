# Scalar type
단 하나의 값만을 저장할 수 있는 데이터 타입
## int
정수형
- prefix에 따라 표시하는 진법이 다르다.
```py
10   # 10
0b10 #  2, prefix '0b'는 bit 2진수          = bin(숫자) 함수
0o10 #  8, prefix '0o'는 octo 8진수         = oct(숫자) 함수
0x10 # 16, prefix '0x'는 hexadecimal 16진수 = hex(숫자) 함수
```
- 다른 타입의 값을 int로 변환한다.
```py
int(3.5)   # 3
int(-3.5)  # -3

int(True)  # 1
int(False) # 0

int("10")  # 10
```
- 진수 변환을 지원한다.  
- ```int(x, base=10)``` 이때 x는 string값이어야 한다.
```py
int("1000", 3) # 27
# 더 자세한 진법 변환은 divmode.md 참조
```
## float
- 지수표기법을 적용할 수 있다.
```py
17e+2     # 1700.0
17e2      # 1700.0
1.672e+2  # 167.2
1.616e-10 # 1.616e-10
```
- float 변환
```py
float(7)     # 7.0
float("1.5") # 1.5

float(True)  # 1.0
float(False) # 0.0
```
- int에는 없는 ```nan(Not a Number)```, ```inf(+무한)```, ```-inf(-무한)```으로 변환된다.
```py
float("nan")  # nan
float("inf")  # inf
float("-inf") # -inf
```
- 실수 + 정수 = 실수
```py
3.0 + 1 # 4.0
```
## None
값이 없음을 의미
- None 입력 (print일시 None, 아닐시 미출력)
```py
a = None
print(a) # None
```
```py
def imNone():
  a = None
  return a
  
imNone() # _
```
- None의 비교
```py
a = None
a is None # True
```
## bool
True, False

- int형을 bool형으로 변환시, 0만 False
```py
bool(0)  # False

bool(1)  # True
bool(2)  # True
bool(-1) # True
```
- float형을 bool형으로 변환시, 0.0만 False
```py
bool(0.0)  # False

bool(0.1)  # True
bool(-1.0) # True
```
- str형을 bool형으로 변환시, empty 값만 False
```py
bool("")    # False
bool("abc") # True
```
- list, set, dictionary 등의 컬렉션 타입에서도, empty 값만 False
```py
bool([])      # False
bool({})      # False

bool([0])     # True
bool({"a":0}) # True
```
# Composite type
두 개 이상의 값을 저장할 수 있는 데이터 타입
