def is_power(a,b):
    if a < b: 
        return False
    elif a%b:
        return False
    elif a == b:
        return True
    else:
        return is_power(a/b,b)

a = int(input('Enter a value for a: '))
b = int(input('Enter a value for b: '))

print(is_power(a,b))