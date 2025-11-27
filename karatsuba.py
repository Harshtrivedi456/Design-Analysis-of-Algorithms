def karatsuba(x,y):
    if x < 10 or y < 10:
        return x * y
    
    m=max(len(str(x)), len(str(y)))
    if(m%2!=0):
        m-=1
        
    a,b=divmod(x, 10**int(m/2))
    c,d=divmod(y, 10**int(m/2))
    ac=karatsuba(a, c)
    bd=karatsuba(b, d)
    abcd=karatsuba(a+b, (c+d))-ac-bd
    return ((ac*(10*m))+bd+(abcd(10**(m//2))))
    
x=int(input("Enter first number1: "))
y=int(input("Enter second number2: "))   
print("Product:", karatsuba(x, y))