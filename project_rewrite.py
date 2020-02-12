def min(x, y):
    if x < y:
        return x
    else:
        return y


def max(x, y):
    if x > y:
        return x
    else:
        return y


def len(iterable):
    x = 0
    for i in str(iterable):
        x += 1
    return x


def multiply(x, y):
    try:
        x, y = int(x), int(y)
        print("Your first number is", x, "and second", y)
        i = 1
        n = 0
        while i <= x:
            n = n + y
            i += 1
        return n
    except ValueError:
        print("These numbers are not digits.")


def pow(x, y):
    
