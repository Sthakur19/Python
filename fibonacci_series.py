# def fibonacci_series(n):
#     a = 0
#     b = 1
#     print(a)
#     while b < n:
#         print(b)
#         # c = a + b 
#         # a = b
#         # b = c 
#         a, b = b, a+b

# fibonacci_series(10)

def fibonacci_series2(n):
    a, b= 0, 1
    print(a)
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c 
        print(b)

fibonacci_series2(7)