#Problem1.6 (!!!!Klar)
#This program calculates products of factors.
product = 1
integer_1 = int(input("Please enter the starting integer: "))
integer_2 = int(input("Please enter the stopping integer: "))
for numbers in range(integer_1, integer_2+1):
    product *= numbers
print(product)