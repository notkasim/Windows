#problem 3.4 (!!!Klar)
def highest(lista):
    list_number = []
    for number in lista:
        list_number.append(number)
        list_number.sort(reverse=True)
        high = list_number[0]
    return high

a1 = highest([5,3])
a2 = highest([2,8,4,3])
a3 = highest([-2,-5])
a4 = highest([42])
print(f"{a1}\n{a2}\n{a3}\n{a4}")


'''def highest(list_numbers):
    the_choosen_one = list_numbers[0]

    for number in list_numbers:

        if number > the_choosen_one:
            the_choosen_one = number
    return the_choosen_one


a1 = highest([5,3])
a2 = highest([2,8,4,3])
a3 = highest([-2,-5])
a4 = highest([42])
print(f"{a1}\n{a2}\n{a3}\n{a4}")'''