def solution(num_list):
    num = sum(i % 2 for i in num_list)
    return [len(num_list) - num, num]
