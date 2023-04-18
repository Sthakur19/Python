def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == False:
        print("Its not prime number")
    else:
        print("Its prime numer")
        

prime_number(7)

