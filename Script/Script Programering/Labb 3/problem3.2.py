# problem 3.2 (!!!Klar)
def closest_to_zero (n1, n2):
    num1 = abs(n1) #num1 = n1 absloute value
    num2 = abs(n2) #num2 = n2 absolute value
    if num1 < num2: #if n1 absolute value is lower then n2 absolute value
        return n1
    else:
        return n2

a1 = closest_to_zero(5,9)
a2 = closest_to_zero(3,-2)
a3 = closest_to_zero(2,2)
print(f"{a1}\n{a2}\n{a3}")