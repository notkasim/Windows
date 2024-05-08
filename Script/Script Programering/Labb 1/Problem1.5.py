#Problem1.5 (!!!Klar)
# This program prints the desired multiplication table
user_input = int(input("What multiplication table would you like to print: "))
factor_1 = int(input("Please enter the starting factor: "))
factor_2 = int(input("Please enter the stopping factor: "))
for numbers in range (factor_1, factor_2+1):
    print(f"{user_input} x {numbers} = {user_input*numbers}")