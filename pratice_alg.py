# somar unidades de um numero inteiro
def digit_sum(x):
    v = str(x)
    result = 0
    for un in v:
        x = int(un)
        result += x
    return result


print digit_sum(434)


# fatorial ######

def factorial(x):
    result = 1
    for i in range(x):
        #print i + 1
        result *= (i + 1)
        #print result
        
    return result


    
print factorial(4)
print 
print factorial(1)
print 
print factorial(3)
print 
