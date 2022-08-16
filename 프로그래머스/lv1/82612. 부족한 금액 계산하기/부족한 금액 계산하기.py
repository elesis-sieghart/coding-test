
def solution(price, money, count):

    # money - (price*1) - (price*2) ... - (price*count) 의 절댓값
    # money - (price*(n(n+1)/2))
    
    if (money - price*count*(count+1)/2) > 0:
        return 0
    else:
        return abs(money - price*count*(count+1)/2)
    
