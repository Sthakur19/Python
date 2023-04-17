def least_find_occurenace(word):
    char = {}
    for key in word:
        if key in char:
            char[key] = char[key] + 1
        else:
            char[key] = 1
    result = min(char, key = char.get)
    print(result)

least_find_occurenace("thethethejkjilkll")

from collections import Counter
word = "hghjgjkhk"
char = Counter(word)
result = min(char, key = char.get)
print(result)

def least_find_occurenace1(word, search_number_of_char):
    char = {}
    for key in word:
        if key in char:
            char[key] = char[key] + 1
        else:
            char[key] = 1
    print(char)
    try:
        print(char[search_number_of_char])
    except:
        print(0)

least_find_occurenace1("thethethejkjilkll", "t")

def least_find_occurenace2(word):
    char = {}
    for key in word:
        if key in char:
            char[key] = char[key] + 1
        else:
            char[key] = 1
    print(char)

least_find_occurenace2("thethethejkjilkll")