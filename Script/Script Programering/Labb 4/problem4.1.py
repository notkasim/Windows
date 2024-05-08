#problem 4.1 (!!!Klar)
def are_equal (the_list, this_list):
    the_list_indexes = len(the_list)
    this_list_indexes = len(this_list)
    if the_list_indexes != this_list_indexes: #if the lists have different length indexses it returns false. 
        return False
    
    for number in range(the_list_indexes): #iterates over the list indexses.
        if the_list[number] != this_list[number]:   #if the_list index != this_list index 
            return False
    return True
    

result = are_equal ([1,2,3], [1,2,3])
result1 = are_equal ([1,2,3], [1,2,4])
result2 = are_equal ([1,2], [1,2,3])

print(result)
print(result1)
print(result2)


'''def are_equal (the_list, this_list):
    the_list_indexes = len(the_list)
    this_list_indexes = len(this_list)
    if the_list_indexes != this_list_indexes: #if the lists have different length it returns false no need to compare each index. 
        return False
    
    for num1, num2 in zip(the_list, this_list):
        if num1 != num2:
            return False
    return True

    

result = are_equal ([1,2,3], [1,2,3])
print(result)'''