# author: LM (AMDG) 12/7/21
def three_letter_words(lst):
    total = 0
    for string in lst:
        if len(string) <= 3:
            total = total + 1
            continue
        else:
            break
    return (total)

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
