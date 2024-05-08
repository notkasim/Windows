#problem 4.2 (!!!Klar)
def change_to_highest(this_list):
    
    for nested_list in this_list:   #iterates over the outerlist
        choosen_numbers = max(nested_list)  #returns the highest number in each nested-list.
        nested_list.clear() #empties the each nested-list
        nested_list.append(choosen_numbers) #adds highest number to each list
        print()
    for indexes in range(len(this_list)): #returns number of items in this_list   
        this_list[indexes] = this_list[indexes][0] # replaceses each sublist with the number in each stored in each sublist. 
    print(this_list)

nest = change_to_highest([[1,3,2],[4,6,5],[9,7,8]])

