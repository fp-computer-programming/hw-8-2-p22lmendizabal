# author: LM(AMDG) 12/6/21

def count_odds(lst):
    total = 0
    for number in lst:
        if number % 2 != 0:
            total += 1
        else:
            continue
    return(total)

print(count_odds([1, 2, 4, 5, 6]))
print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
