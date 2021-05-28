def ly(x):
    if x % 4 == 0:
        if x % 100 == 0:
            return "Is not a leap year"
        return "Is a leap year"
    else:
        return "Is not a leap year"