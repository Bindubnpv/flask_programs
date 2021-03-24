class Error(Exception):
    pass

class ErrorLimit(Error):
    pass

class ErrorForSub(Error):
    pass

'''    
a = int(input('enter first number:'))
b = int(input('enter second number:'))
def fun():
    try:
        if a<0 or b<0:
            raise ErrorForValue('entered num is not an integer')
        elif a == 0 or b == 0:
            raise ErrorForDivision('value should be greater than zero')

    except ErrorForValue as v:
        print(v)

    except ErrorForDivision as z:
        print(z) 
    
fun()    
'''