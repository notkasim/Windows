#problem 3.1 (!!!Klar)
def abs(number):
    zero = 0
    if number < zero:
        return zero - number #calculates the positive number of number (--=+) 
    else:
        return number
print(abs(-5))
print(abs(5))
print(abs(0))