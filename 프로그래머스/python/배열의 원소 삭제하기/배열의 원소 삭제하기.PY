def solution(arr, delete_list):
    b = set(delete_list)
    a = []

    for i in arr:
        if i not in b:
            a.append(i)

    return a