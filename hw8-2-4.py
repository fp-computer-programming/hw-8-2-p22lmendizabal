# author: LM (AMDG) 12/7/21
def number_of_letters(word, letter):
    total = 0
    for x in word:
        if x == letter:
            total += 1
    return total

number_of_letters("cat", "t")
print(number_of_letters("cat", "t") == 1)
print(number_of_letters("apple", "p") == 2)
print(number_of_letters("supercalifragilisticexpialidocious", "i") == 7)