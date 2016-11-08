# somar unidades de um numero inteiro
def digit_sum(x):
    v = str(x)
    result = 0
    for un in v:
        x = int(un)
        result += x
    return result


print digit_sum(434)
