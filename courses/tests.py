def decor(function):
    list_of_numbers = range(10)

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@decor
def numbers_printer():
    for number in list_of_numbers:
        print(number)


numbers_printer()
