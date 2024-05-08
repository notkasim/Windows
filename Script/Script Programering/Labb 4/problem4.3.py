#Problem 4.3 (!!!Klar)
def sum (the_list):
    this_dict = {'All': 0, 'Even':0, 'Odd':0}
    for number in the_list:
        this_dict['All'] += number

        if number % 2 == 0:
            this_dict["Even"] += number
        else:
            this_dict['Odd'] += number

    return f"{this_dict}"
        
this_list = sum([1,2,3,4,5])
print(this_list)