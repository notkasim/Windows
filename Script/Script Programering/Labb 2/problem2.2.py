# problem2.2 (!!!Klar)
# this function calculates the sum and average number of a list of numbers. 
def average (sequence):
    total = sum(sequence)
    average = total // len(sequence)
    return average
print(f"The average number is: {average([1,4,4])}")
