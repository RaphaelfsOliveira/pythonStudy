
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2 , x):
            
            if x % n == 0:
                print x , "%", n, "=", x%n
                return False
                
        print x , "%", n, "=", x%n
        return True
 
 
 
 
    
"""
print is_prime(3)
print is_prime(2)
print is_prime(4)
print is_prime(0)
print is_prime(1)
"""
print
print is_prime(9)
print
print is_prime(-10)

