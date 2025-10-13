def solution(money):
    price=5500
    ice=money//price
    change=money-price*ice
    result=[ice,change]
    return result
    