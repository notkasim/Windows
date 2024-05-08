#Problem 2.5 (!!!Klar)
def string_with_numbers (string):
    start_value = str(1)
    for numbers in range (2,string+1):
        numbers = str(numbers)
        start_value = f"{start_value}_{numbers}"
    return f"\'{start_value}\'"
print(string_with_numbers(5))