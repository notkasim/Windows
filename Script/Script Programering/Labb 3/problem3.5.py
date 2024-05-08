# problem 3.5 (!!!Klar)
def count(list_str, string):
    amount = 0
    for this_many_times in list_str: #Iterates over the list_str
        if this_many_times == string:   #When this_many_times == string
            this_many_times = 1         #Then this_many_times = 1
            amount += this_many_times
    return amount         
print(count(["a","b","c"], ("b")))
print(count(["a","b","c"], ("e")))
print(count(["a","a","a"], ("a")))