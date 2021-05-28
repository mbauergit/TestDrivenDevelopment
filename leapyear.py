def ly(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return "Is a leap year"
            return "Is not a leap year"
        return "Is a leap year"
    else:
        return "Is not a leap year"