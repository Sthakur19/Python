# def string_modification(string):
#     empty_string = []
#     temp = string.split("_")
#     for i in temp:
#         empty_string.append(i[0].lower() + i[1:].upper())
#         string = ".".join(empty_string)
#     print(string)
# string_modification("This_Is_a_String")


def string_modification(string):
    empty_string = " "
    temp = string.split("_")
    for i in temp:
        empty_string = empty_string + i[0].lower() + i[1:].upper() + "."
    empty_string = empty_string[:-1]
    print(empty_string)
string_modification("This_Is_a_String")