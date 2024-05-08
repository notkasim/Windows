class Calculator:
    def __init__(self, initial_mem_value):
        self.memory_value = [initial_mem_value]

    def get_memory_value(self):
        return self.memory_value[-1]
    
    def add(self, number):
        current = self.get_memory_value()
        new_mem_value = current + number
        self.memory_value.append(new_mem_value)
        return self.memory_value[-1]
    
    def subtract(self, number):
        current = self.get_memory_value()
        new_mem_value = current - number
        self.memory_value.append(new_mem_value)
        return self.memory_value[-1]
    
    def multiply(self, number):
        current = self.get_memory_value()
        new_mem_value = current * number
        self.memory_value.append(new_mem_value)
        return self.memory_value[-1]
    
    def divide(self, number):
        current = self.get_memory_value()
        new_mem_value = current // number
        self.memory_value.append(new_mem_value)
        return self.memory_value[-1]
    
    def undo(self):
        self.memory_value.pop()
        return self.memory_value[-1]
    
    def can_undo(self):
        return True if len(self.memory_value) > 1 else False
    

#Loop
initial_memory_value = int(input("Enter initial memory value: "))
calculator = Calculator(initial_memory_value)

operation = ""

while operation != "quit":
	
	operation = input("Enter operation (add/sub/mul/div/undo/quit): ")
	
	if operation == "undo":
		if calculator.can_undo():
			calculator.undo()
			print(str(calculator.get_memory_value())+" is stored in memory.")
		else:
			print("There is nothing to undo.")
	elif operation != "quit":
		
		operand = int(input("Enter operand: "))
		
		if operation == "add":
			calculator.add(operand)
		elif operation == "sub":
			calculator.subtract(operand)
		elif operation == "mul":
			calculator.multiply(operand)
		elif operation == "div":
			calculator.divide(operand)
		
		print(str(calculator.get_memory_value())+" is stored in memory.")

print("The program finished with "+str(calculator.get_memory_value())+" in memory.")