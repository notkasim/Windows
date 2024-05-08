#problem2.6 (!!!Klar)
def xxx (interger):
    total_sum = 0
    count_list = []
    for number in range (1,interger+1):
        total_sum += number*number #calculates the sum of all the numbers
        int_to_str = str(number) #converts number to str(number)
        str_number = "+".join(int_to_str*number) #adds "+" between each string charecter
        count_list.append(str_number) # adds the value stored in str_number to count_list
        calculation = " + ".join(count_list) #adds "+" between each string in the list
    return f"{calculation} --> {total_sum}"

a1 = xxx(1)
a2 = xxx(2)
a3 = xxx(3)
a4 = xxx(4)
print(f"{a1}\n{a2}\n{a3}\n{a4}")