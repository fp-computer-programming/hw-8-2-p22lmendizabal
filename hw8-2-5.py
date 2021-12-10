# author: LM (AMDG) 12/7/21
def adding_numbers(lst):
    total = 0
    for number in lst:
        if number % 2 != 0:
            total += 0
            print(total)
            break
        elif number % 2 == 0:
            total = number + total
    return total


adding_numbers([9, 10, 4, 6, 8])
print(adding_numbers([2, 4, 6, 8, 9]) == 20)
print(adding_numbers([13, 12, 10]) == 0)
print(adding_numbers([14, 16, 32]) == 62)