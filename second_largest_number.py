def second_largest_number(my_list):
    # my_list.sort()
    # print(my_list[-2])

    new_list = set(my_list)
    new_list.remove(max(new_list))
    max(new_list)
    print(max(new_list))

second_largest_number([3,4,59,96,96,7,18])

