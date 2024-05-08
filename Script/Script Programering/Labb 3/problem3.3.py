# problem 3.3 (!!!Klar)
def closest_to_zero_4 (n1, n2, n3, n4):
    zero = 0
    arguments = [n1, n2, n3, n4] #makes a list out of the numbers. 
    close = arguments[0] #close har förta värdet av listan argument.
    for number in arguments:
            if number == zero:
                 return zero
            elif abs(number) < abs(close): #compares the absolute value of the numbers and assignes the lowest number to close.  
                close = number
    return close
zero_close_1 = closest_to_zero_4(-5, -7, -3, 10)
zero_close_2 = closest_to_zero_4(5, 9, 2, 11)
zero_close_3 = closest_to_zero_4(0, 3, -2, 4)
zero_close_4 = closest_to_zero_4(2, 2, -2, 1)

print(f"{zero_close_1}\n{zero_close_2}\n{zero_close_3}\n{zero_close_4}")