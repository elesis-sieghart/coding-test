# 리스트 원소 추가
## append
원소 마지막에 추가
```py
a = [1, 2]
a.append(3) # [1, 2, 3]
```
## insert
```리스트.index(입력할index, 값)```
```py
a = [1, 3]
a.insert(1, 2) # [1, 2, 3]
```
## `+` 연산자
```py
a = [1, 2]
b = [3, 4]
a + b # [1, 2, 3, 4]

a += [3, 4] # [1, 2, 3, 4]
```
## extend
```리스트.extend(추가할리스트)```
```py
a = [1]
a.extend([2, 3]) # [1, 2, 3]
```
# 리스트 원소 삭제
## del
```del 리스트[인덱스]```
```py
a = [1, 2, 3]
del a[2] # [1, 2]
```
## remove
```list.remove(찾을아이템)```
```py
a = [1, 2, 3]
a.remove(2) # [1, 3]
a.remove(5) # ValueError
```
#### del과 index 혼합 사용시 remove 효과가 난다.
```py
a = [1, 2, 3]
del a[a.index(2)] # [1, 3]
```
