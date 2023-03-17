def calc(*args):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    return result


# TypeError: calc() got an unexpected keyword argument 'a'
print(calc(a=1, b=2, c=3))
