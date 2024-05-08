#problem 3.7 (!!!Klar)
def simple_calculater ():
    stored_memory = int(input("initial memory value: "))
    operation = "" #empty string to initialize the while loop. 
    while operation != "quit": #keep looping as long as operation is not equal to "quit"
        operation = input("Enter operation (add/sub/mul/div/quit): ")

        if operation == "add":
            number = int(input("Enter operand: "))
            stored_memory += number
            print(f"{stored_memory} is stored in memory.")

        elif operation == "mul":
            number = int(input("Enter operand: "))
            stored_memory *= number
            print(f"{stored_memory} is stored in memory.")

        elif operation == "sub":
            number = int(input("Enter operand: "))
            stored_memory -= number
            print(f"{stored_memory} is stored in memory.")

        elif operation == "div":
            number = int(input("Enter operand: "))
            stored_memory //= number
            print(f"{stored_memory} is stored in memory.")
            
    return f"The program finished with {stored_memory} stored in memory."

calculated_result = simple_calculater()
print(f"{calculated_result}")