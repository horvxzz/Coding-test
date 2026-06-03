def solution(num_list, n):
    a=num_list[n::]
    del num_list[n:]
    return a+num_list