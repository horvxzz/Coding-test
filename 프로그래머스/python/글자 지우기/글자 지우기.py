def solution(my_string, indices):
    a = ""
    for i in range(len(my_string)):
        if i not in indices:
            a += my_string[i]
    return a