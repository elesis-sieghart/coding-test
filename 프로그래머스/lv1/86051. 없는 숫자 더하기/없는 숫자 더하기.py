def solution(numbers):
    val = 45
    for i in numbers:
        val = val - i
    return val


# sum
def solution(numbers):
    return 45 - sum(numbers)

# lambda
solution = lambda x: sum(range(10)) - sum(x)
