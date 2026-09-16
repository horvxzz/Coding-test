def solution(my_string,overwrite_string,s):
    a=my_string[:s]
    b=my_string[s+len(overwrite_string):]
    return a+overwrite_string+b