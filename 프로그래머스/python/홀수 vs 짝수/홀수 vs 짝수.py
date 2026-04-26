def solution(num_list):
    a = sum(num_list[0::2])
    b = sum(num_list[1::2])
    return max(a, b)