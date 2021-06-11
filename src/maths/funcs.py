def factorial(number):
    if number > 1:
        return factorial(number-1)*number
    elif number < 1:
        return ("NAN")
    else:
        return 1


def fib(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    elif number > 2:
        return fib(number-1) + fib(number-2)
    else:
        return ("NAN")