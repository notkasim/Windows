#problem3.6 (!!!Klar)
user_input1 = int(input("Enter a number: "))
user_input2 = int(input("Enter a number: "))

def summerizing_even_intergers (int1, int2):
    zero = 0
    
    if int1 > int2:
        return f"The first number should be lower then the second number."
    else:   
        interger_sum = 0
        for number in range (int1, int2 +1):
            if number % 2 == zero:
                interger_sum += number
        return interger_sum
    #else:
    #    return f"The two numbers should be even numbers."

sum_even = summerizing_even_intergers(user_input1, user_input2)
print (sum_even)