def factorial(number):
    if number > 1:
        return factorial(number-1)*number
    elif number < 1:
        return ("NAN")
    else:
        return 1