
# packing, unpacking
### packing
인자로 받은 여러개의 값을 하나의 객체로 합쳐 받을 수 있게 해준다.
즉 어떠한 함수를 정의할때 ```def function(*arg):```와 같은 식으로 하면, 인자가 몇개가 오던지
그 인자를 하나의 객체로 합쳐준다.

```py
# packing
num = (1, 2)


# unpacking
a = (1, 2, 'a')
print(*a) # 1 2 

num = 1, 2, 3, 4, 5
n1, n2, *others = num
print(others) # [3, 4, 5, 6, 7]
```
