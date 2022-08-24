# range
range() 함수의 결과는 **반복가능(iterable)** 하기 때문에 **for문을 사용해 출력** 할 수 있다.

## range(stop)
```py
# range(10)
range(10) 

# [0, 2, ..., 9]
list(range(10)) 
```

## range(start, stop)
```py
# [1, 2, ..., 10]
list(range(1, 11)) 
```

## range(start, stop, step)
step은 숫자의 간격을 나타낸다.
```py
# [0, 2, 4, 6, 8]
list(range(0, 10, 2))

# [10, 9, ..., 1]
list(range(10, 0, -1))
```
