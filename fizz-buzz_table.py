# Create a function called fizz_buzz_table that takes a positive integer (n) as an input,
#  and returns the n x n multiplication table in a two dimensional array, where the “fizz-buzz” 
#  numbers are represented by their “fizz-buzz” string.
# A number is a “fizz-buzz” number if it’s a multiple of 3 or 5. If it’s a multiple of 3, it’s value should be Fizz.
#  If it’s a multiple of 5, it’s value should be Buzz. If it’s a multiple of both 3 and 5, it’s value should be FizzBuzz.

# def fizz_buzz_table(n):
#     print("[", end="\n")
#     for i in range(1, n+1):
#         print("[", end="")
#         for j in range(1, n+1):
#             c= i*j
#             if c % 3 == 0 and c % 5 == 0:
#                 print("FizzBuzz" , end=", ")
#             elif c % 3 == 0:
#                 print("Fizz",  end=", ")
#             elif c % 5 == 0:
#                 print("Buzz" ,  end=", ")
#             else:
#                 print(c, end=", ")
#         print("]", end="")
#         print("\n")
#     print("]", end=", ")
# fizz_buzz_table(5)


# table = []
# for y in range(1, 6):
#     sub_table = []
#     for x in range(1, 6):
#         sub_table.append(x*y)
#     table.append(sub_table)

# for t in table:
#     print(t)


def fizz_buzz_table(n):
    my_fizz_buzz_table = []
    for i in range(1, n+1):
        my_fizz_buzz_sub_table = []
        for j in range(1, n+1):
            multiplecation_number = i*j
            if multiplecation_number % 3 == 0 and multiplecation_number % 5 == 0:
                multiplecation_number = "FizzBuzz"
            elif multiplecation_number % 3 == 0:
                multiplecation_number = "Fizz"
            elif multiplecation_number % 5 == 0:
                multiplecation_number = "Buzz"
            my_fizz_buzz_sub_table.append(multiplecation_number)
        my_fizz_buzz_table.append(my_fizz_buzz_sub_table)  
    print("[", end="\n")
    for z in my_fizz_buzz_table:
        print(" ",z)
    print("]", end="\n")
fizz_buzz_table(5)
fizz_buzz_table(3)