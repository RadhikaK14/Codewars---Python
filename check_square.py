import math

def is_square(n): 
    status = False
    if (n >= 0):
        square_root = math.sqrt(n)
        if square_root.is_integer() == True:
            status = True
        
    return status

x = int(input ('Enter a number : '))
return_status = is_square(x)
if return_status == True:
    print(f'{x} is a Perfect square')
else:
    print(f'{x} is not a Perfect square')