def reverse(x):
    sign = -1 if x < 0 else 1
    reversed_x = int(str(abs(x))[::-1])
    if reversed_x > 2**31 - 1:
        return 0
    return sign * reversed_x
