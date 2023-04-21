# def prime_number(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == False:
#         print("Its not prime number")
#     else:
#         print("Its prime numer")
        

# prime_number(7)


def display_prime_number(start, end):
    for num in range(start, end):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    print(num)

display_prime_number(10, 100)