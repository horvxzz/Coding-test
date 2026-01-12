def solution(my_string):
    nums = []
    for ch in my_string:
        if ch.isdigit():
            nums.append(int(ch))
    nums.sort()
    return nums
