def solution(my_string):
    for s in 'aeiou':
        my_string = my_string.replace(s, '')
    return my_string
