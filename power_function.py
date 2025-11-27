# iterative version
def power_function(base, exponent):

    for i in range(exponent):
        result=0
        result = base ** exponent            
    return base ** exponent

base=3
exponent=4

print(power_function(base, exponent))  

# recursive version
def power_function_recursive(base, exponent):
    if exponent == 0:                     #T(n) = 1
        return 1
    else:
        return base * power_function_recursive(base, exponent - 1) #T(n) = T(n-1) + 1

print(power_function_recursive(2,5))