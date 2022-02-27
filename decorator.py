def decorator(f):
    def wraps(*args, **kwargs):
        print(f"начата работа функиции{f}")
        result = f(*args, **kwargs)
        print(f"Завершена работа функции{f}")
        return result

    return wraps


@decorator
def add(a, b):
    return a + b


add(10, 23)
