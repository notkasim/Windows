#problem 1.3 (!!!Klar)
sum = 0
user_input = int(input("How many numbers would you like to enter? "))
for numbers in range (user_input):
    numbers_input = int(input("write a number:"))
    sum += numbers_input
    average = sum // user_input
print(f"The average value of these {user_input} numbers is: {average} ")




